
TEMPLATE_TYPE_BUTTON = 'button'
TEMPLATE_TYPE_GENERIC = 'generic'


class TemplateElement(object):

    def __init__(self, title, subtitle=None, item_url=None, image_url=None, buttons=None):
        assert len(title) < 81, 'Title limit of 80 chars reached'
        if subtitle is not None:
            assert len(subtitle) < 81, 'Subtitle limit of 80 reached'
        if buttons is not None:
            assert len(buttons) < 4, 'You can only have 3 buttons in an element'

        self.title = title
        self.subtitle = subtitle
        self.item_url = item_url
        self.image_url = image_url
        self.buttons = buttons
        if buttons is None:
            self.buttons = []

    def to_dict(self):
        response = {'title': self.title}
        if self.subtitle is not None:
            response.update({'subtitle': self.subtitle})
        if self.item_url is not None:
            response.update({'item_url': self.item_url})
        if self.image_url is not None:
            response.update({'image_url': self.image_url})
        if len(self.buttons):
            response.update({'buttons': [b.to_dict() for b in self.buttons]})
        return response


class GenericTemplate(object):

    def __init__(self, elements):
        self.elements = elements

    def to_dict(self):
        return {
            'type': 'template',
            'payload': {
                'template_type': TEMPLATE_TYPE_GENERIC,
                'elements': [
                    e.to_dict() for e in self.elements
                ]
            }
        }


class ButtonTemplate(object):

    def __init__(self, text, buttons):
        self.text = text
        self.buttons = buttons

    def to_dict(self):
        return {
            'type': 'template',
            'payload': {
                'template_type': TEMPLATE_TYPE_BUTTON,
                'text': self.text,
                'buttons': [
                    b.to_dict() for b in self.buttons
                ]
            }
        }
