import pytest

from messenger.models import GenericTemplate, TemplateElement
from messenger.models.button import UrlButton
from messenger.models.templates import TEMPLATE_TYPE_GENERIC


class TestElement(object):
    mock_title = 'mock-title'
    mock_subtitle = 'mock-subtitle'
    mock_item_url = 'http://mock-item-url/'
    mock_image_url = 'http://mock-image-url/'

    def test_create_minimal(self):
        e = TemplateElement(self.mock_title)

        assert self.mock_title == e.title

    def test_to_dict_minimal(self):
        e = TemplateElement(self.mock_title)

        e_dict = e.to_dict()

        assert self.mock_title == e_dict['title']

    def test_create_with_subtitle(self):
        e = TemplateElement(self.mock_title, subtitle=self.mock_subtitle)

        assert self.mock_title == e.title
        assert self.mock_subtitle == e.subtitle

    def test_to_dict_with_subtitle(self):
        e = TemplateElement(self.mock_title, subtitle=self.mock_subtitle)

        e_dict = e.to_dict()

        assert self.mock_title == e_dict['title']
        assert self.mock_subtitle == e_dict['subtitle']

    def test_create_with_item_url(self):
        e = TemplateElement(self.mock_title, item_url=self.mock_item_url)

        assert self.mock_title == e.title
        assert self.mock_item_url == e.item_url

    def test_to_dict_with_item_url(self):
        e = TemplateElement(self.mock_title, item_url=self.mock_item_url)

        e_dict = e.to_dict()

        assert self.mock_title == e_dict['title']
        assert self.mock_item_url == e_dict['item_url']

    def test_create_with_image_url(self):
        e = TemplateElement(self.mock_title, image_url=self.mock_image_url)

        assert self.mock_title == e.title
        assert self.mock_image_url == e.image_url

    def test_to_dict_with_image_url(self):
        e = TemplateElement(self.mock_title, image_url=self.mock_image_url)

        e_dict = e.to_dict()

        assert self.mock_title == e_dict['title']
        assert self.mock_image_url == e_dict['image_url']

    def test_create_with_button(self):
        mock_button_title, mock_button_url = 'mock-button-title', 'test://mock-button-url/'
        e = TemplateElement(self.mock_title, buttons=[UrlButton(mock_button_title, mock_button_url)])

        assert self.mock_title == e.title
        assert mock_button_title == e.buttons[0].title
        assert mock_button_url == e.buttons[0].url

    def test_to_dict_with_button(self):
        mock_button_title, mock_button_url = 'mock-button-title', 'test://mock-button-url/'
        e = TemplateElement(self.mock_title, buttons=[UrlButton(mock_button_title, mock_button_url)])

        e_dict = e.to_dict()

        assert self.mock_title == e_dict['title']
        assert mock_button_title == e_dict['buttons'][0]['title']
        assert mock_button_url == e_dict['buttons'][0]['url']

    def test_create_failed_title(self):
        with pytest.raises(AssertionError):
            TemplateElement('#' * 81)

    def test_create_failed_subtitle(self):
        with pytest.raises(AssertionError):
            TemplateElement(self.mock_title, subtitle='#' * 81)

    def test_create_failed_buttons(self):
        with pytest.raises(AssertionError):
            mock_button_title, mock_button_url = 'mock-button-title', 'test://mock-button-url/'
            TemplateElement(self.mock_title, buttons=[
                UrlButton(mock_button_title, mock_button_url),
                UrlButton(mock_button_title, mock_button_url),
                UrlButton(mock_button_title, mock_button_url),
                UrlButton(mock_button_title, mock_button_url)
            ])


class TestGenericTemplate(object):
    mock_first_element_title = 'mock-first-element-title'
    mock_second_element_title = 'mock-second-element-title'

    def test_create_minimal(self):
        gt = GenericTemplate(elements=[])

        assert 0 == len(gt.elements)

    def test_to_dict_minimal(self):
        gt = GenericTemplate(elements=[])

        gt_dict = gt.to_dict()

        assert 'template' == gt_dict['type']
        assert gt_dict.get('payload') is not None
        assert TEMPLATE_TYPE_GENERIC == gt_dict['payload']['template_type']
        assert 0 == len(gt_dict['payload']['elements'])

    def test_create_single_element(self):
        gt = GenericTemplate(elements=[TemplateElement(self.mock_first_element_title)])

        assert 1 == len(gt.elements)

    def test_to_dict_single_element(self):
        gt = GenericTemplate(elements=[TemplateElement(self.mock_first_element_title)])

        gt_dict = gt.to_dict()

        assert 1 == len(gt_dict['payload']['elements'])
        assert self.mock_first_element_title == gt_dict['payload']['elements'][0]['title']

    def test_create_multiple_elements(self):
        gt = GenericTemplate(elements=[
            TemplateElement(self.mock_first_element_title),
            TemplateElement(self.mock_second_element_title)
        ])

        assert 2 == len(gt.elements)

    def test_to_dict_multiple_elements(self):
        gt = GenericTemplate(elements=[
            TemplateElement(self.mock_first_element_title),
            TemplateElement(self.mock_second_element_title)
        ])

        gt_dict = gt.to_dict()

        assert 2 == len(gt_dict['payload']['elements'])
        assert self.mock_first_element_title == gt_dict['payload']['elements'][0]['title']
        assert self.mock_second_element_title == gt_dict['payload']['elements'][1]['title']
