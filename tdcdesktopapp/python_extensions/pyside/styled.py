from PySide6.QtWidgets import QWidget


def styled(widget: QWidget, style_name) -> QWidget:
    """Apply style name to widget

    Styles are defined in css as style property `QLabel[style="message-small"]`"""
    widget.setProperty("style", style_name)
    widget.style().unpolish(widget)
    widget.style().polish(widget)
    return widget
