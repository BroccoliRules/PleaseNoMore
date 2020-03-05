from tethys_sdk.base import TethysAppBase, url_map_maker


class AboutMe(TethysAppBase):
    """
    Tethys app class for About Me.
    """

    name = 'About Me'
    index = 'about_me:home'
    icon = 'about_me/images/icon.gif'
    package = 'about_me'
    root_url = 'about-me'
    color = '#2980b9'
    description = ''
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='about-me',
                controller='about_me.controllers.home'
            ),

            UrlMap(
                name='map',
                url='about-me/map',
                controller='about_me.controllers.map'
            ),
        )
        return url_maps
