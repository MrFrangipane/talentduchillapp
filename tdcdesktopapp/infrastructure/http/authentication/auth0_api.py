from auth0.authentication.token_verifier import TokenVerifier, AsymmetricSignatureVerifier
import jwt
import requests


class Auth0API:
    ALGORITHMS = ['RS256']

    def __init__(self, domain, client_id, audience):
        self._domain = domain
        self._client_id = client_id
        self._audience = audience

        self._token_payload = None

        self.device_code = None
        self.verification_uri = None

        self.polling_interval = None
        self.current_user = None
        self.access_token = None

    def get_device_code(self):
        device_code_payload = {
            'client_id': self._client_id,
            'scope': 'openid profile',
            'audience': self._audience
        }
        device_code_response = requests.post(f'https://{self._domain}/oauth/device/code', data=device_code_payload)

        if device_code_response.status_code != 200:
            raise ValueError('Error generating the device code')

        device_code_data = device_code_response.json()
        self.device_code = device_code_data['user_code']
        self.verification_uri = device_code_data['verification_uri_complete']
        self.polling_interval = device_code_data['interval']

        self._token_payload = {
            'grant_type': 'urn:ietf:params:oauth:grant-type:device_code',
            'device_code': device_code_data['device_code'],
            'client_id': self._client_id
        }

    def check_authenticated(self):
        token_response = requests.post(f"https://{self._domain}/oauth/token", data=self._token_payload)
        token_data = token_response.json()

        if token_response.status_code == 200:
            self._validate_token(token_data['id_token'])
            self.current_user = jwt.decode(
                token_data['id_token'],
                algorithms=Auth0API.ALGORITHMS,
                options={"verify_signature": False}
            )
            self.access_token = token_data['access_token']
            return True

        elif token_data['error'] not in ('authorization_pending', 'slow_down'):
            raise PermissionError(token_data['error_description'])

        else:
            return False

    def _validate_token(self, id_token):
        jwks_url = f"https://{self._domain}/.well-known/jwks.json"
        issuer = f"https://{self._domain}/"
        signature_verifier = AsymmetricSignatureVerifier(jwks_url)
        token_verifier = TokenVerifier(signature_verifier=signature_verifier, issuer=issuer, audience=self._client_id)
        token_verifier.verify(id_token)
