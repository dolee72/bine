from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns

from bine.views import BookList, BookNoteList, BookNoteDetail, \
    BookNoteLikeItUpdate, BookNoteReplyDetail, BookNoteReplyList, BookSearch, \
    Login, Register, IndexView


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', IndexView.as_view()),
    url(r'^auth/login/', Login.as_view()),
    url(r'^auth/register/', Register.as_view()),
    url(r'^book/$', BookList.as_view()),
    url(r'^book/search/$', BookSearch.as_view()),
    url(r'^note/$', BookNoteList.as_view()),
    url(r'^note/(?P<pk>[0-9]+)/$', BookNoteDetail.as_view()),
    url(r'^note/(?P<note_id>[0-9]+)/reply/$', BookNoteReplyList.as_view()),
    url(r'^note/(?P<note_id>[0-9]+)/reply/(?P<reply_id>[0-9]+)/$', BookNoteReplyDetail.as_view()),
    url(r'^note/(?P<note_id>[0-9]+)/likeit/', BookNoteLikeItUpdate.as_view()),
    url(r'^api-token-auth/', 'rest_framework_jwt.views.obtain_jwt_token'),
    url(r'^api-token-refresh/', 'rest_framework_jwt.views.refresh_jwt_token'),
    # url(r'^.*$', RedirectView.as_view(url='/static/bine/html/bine.html#/note/')),

]

urlpatterns = format_suffix_patterns(urlpatterns)