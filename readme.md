# TDC Desktop App

Basic accounting application for small associations

## Zero configuration testing

All is stored in RAM, nothing is saved on quit

````
python -m tdcdesktopapp --persistence ram
````

## Use with API

````
python -m tdcdesktopapp --persistence http --api-host HOST --auth0-configuration auth0.json
````

Replace `HOST` with API host like `127.0.0.1:8000` for local testing

File `auth0.json` being

````json
{
  "domain": "XXXX",
  "client_id": "XXXX",
  "audience": "XXXX"
}
````

## Notes

- https://www.rasmussen.edu/degrees/business/blog/basic-accounting-terms-acronyms-and-abbreviations-students-should/
- https://herbertograca.com/2017/11/16/explicit-architecture-01-ddd-hexagonal-onion-clean-cqrs-how-i-put-it-all-together/#more-14874
- https://aiven.io/blog/introduction-to-event-based-programming
- https://www.figma.com/blog/how-figmas-multiplayer-technology-works/
- https://stackoverflow.com/questions/67560009/how-can-i-send-incoming-messages-from-web-socket-to-worker-thread
- https://github.com/ets-labs/python-dependency-injector
