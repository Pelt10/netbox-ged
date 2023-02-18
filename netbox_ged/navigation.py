from extras.plugins import PluginMenuItem, PluginMenu, PluginMenuButton
from utilities.choices import ButtonColorChoices
from django.conf import settings

menuitem = [
    PluginMenuItem(
        link='plugins:netbox_ged:document_list',
        link_text='Documents',
        buttons=[PluginMenuButton(
            link='plugins:netbox_ged:document_add',
            title='Add',
            icon_class='mdi mdi-plus-thick',
            color=ButtonColorChoices.GREEN
        )]
    ),
    PluginMenuItem(
        link='plugins:netbox_ged:documenttype_list',
        link_text='Document Types',
        buttons=[PluginMenuButton(
            link='plugins:netbox_ged:documenttype_add',
            title='Add',
            icon_class='mdi mdi-plus-thick',
            color=ButtonColorChoices.GREEN
        )]
    ),
]

# If we are using NB 3.4.0+ display the new top level navigation option
if settings.VERSION >= '3.4.0':

    menu = PluginMenu(
        label='Documents',
        groups=(
            ('Document Storage', menuitem),
        ),
        icon_class='mdi mdi-file-document-multiple'
    )

else:

    # Fall back to pre 3.4 navigation option
    menu_items = menuitem
