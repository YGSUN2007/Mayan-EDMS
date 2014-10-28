from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _

from documents.permissions import PERMISSION_DOCUMENT_TYPE_EDIT

from .permissions import (PERMISSION_METADATA_DOCUMENT_EDIT,
                          PERMISSION_METADATA_DOCUMENT_VIEW,
                          PERMISSION_METADATA_TYPE_CREATE,
                          PERMISSION_METADATA_TYPE_DELETE,
                          PERMISSION_METADATA_TYPE_EDIT,
                          PERMISSION_METADATA_TYPE_VIEW)

metadata_edit = {'text': _(u'Edit metadata'), 'view': 'metadata:metadata_edit', 'args': 'object.pk', 'famfam': 'xhtml_go', 'permissions': [PERMISSION_METADATA_DOCUMENT_EDIT]}
metadata_view = {'text': _(u'Metadata'), 'view': 'metadata:metadata_view', 'args': 'object.pk', 'famfam': 'xhtml_go', 'permissions': [PERMISSION_METADATA_DOCUMENT_VIEW], 'children_view_regex': ['metadata']}
metadata_multiple_edit = {'text': _(u'Edit metadata'), 'view': 'metadata:metadata_multiple_edit', 'famfam': 'xhtml_go', 'permissions': [PERMISSION_METADATA_DOCUMENT_EDIT]}

setup_document_type_metadata = {'text': _(u'Metadata'), 'view': 'metadata:setup_document_type_metadata', 'args': 'document_type.pk', 'famfam': 'xhtml', 'permissions': [PERMISSION_DOCUMENT_TYPE_EDIT]}

setup_metadata_type_list = {'text': _(u'Metadata types'), 'view': 'metadata:setup_metadata_type_list', 'famfam': 'xhtml_go', 'icon': 'xhtml.png', 'permissions': [PERMISSION_METADATA_TYPE_VIEW]}
setup_metadata_type_edit = {'text': _(u'Edit'), 'view': 'metadata:setup_metadata_type_edit', 'args': 'object.pk', 'famfam': 'xhtml', 'permissions': [PERMISSION_METADATA_TYPE_EDIT]}
setup_metadata_type_delete = {'text': _(u'Delete'), 'view': 'metadata:setup_metadata_type_delete', 'args': 'object.pk', 'famfam': 'xhtml_delete', 'permissions': [PERMISSION_METADATA_TYPE_DELETE]}
setup_metadata_type_create = {'text': _(u'Create new'), 'view': 'metadata:setup_metadata_type_create', 'famfam': 'xhtml_add', 'permissions': [PERMISSION_METADATA_TYPE_CREATE]}
