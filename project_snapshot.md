# Project Snapshot: hexo-nsfw-nsfw

## 1. Directory Structure
```text
hexo-nsfw-nsfw/
  .gitignore
  .gitmodules
  _config.butterfly.yml
  _config.yml
  package.json
  .github/
    dependabot.yml
  scaffolds/
    draft.md
    page.md
    post.md
    post.md.bak
  source/
  themes/
    .gitkeep
    butterfly/
      .gitignore
      LICENSE
      README.md
      README_CN.md
      _config.yml
      package.json
      plugins.yml
      .github/
        FUNDING.yml
        ISSUE_TEMPLATE/
          bug_report.yml
          config.yml
          feature_request.yml
        workflows/
          publish.yml
          stale.yml
      languages/
        default.yml
        en.yml
        ja.yml
        ko.yml
        zh-CN.yml
        zh-HK.yml
        zh-TW.yml
      layout/
        archive.pug
        category.pug
        index.pug
        page.pug
        post.pug
        tag.pug
        includes/
          additional-js.pug
          footer.pug
          head.pug
          layout.pug
          pagination.pug
          rightside.pug
          sidebar.pug
          head/
            Open_Graph.pug
            analytics.pug
            config.pug
            config_site.pug
            google_adsense.pug
            preconnect.pug
            pwa.pug
            site_verification.pug
            structured_data.pug
          header/
            index.pug
            menu_item.pug
            nav.pug
            post-info.pug
            social.pug
          loading/
            fullpage-loading.pug
            index.pug
            pace.pug
          mixins/
            article-sort.pug
            indexPostUI.pug
          page/
            404.pug
            categories.pug
            default-page.pug
            flink.pug
            shuoshuo.pug
            tags.pug
          post/
            outdate-notice.pug
            post-copyright.pug
            reward.pug
          third-party/
            aplayer.pug
            effect.pug
            pjax.pug
            prismjs.pug
            subtitle.pug
            umami_analytics.pug
            abcjs/
              abcjs.pug
              index.pug
            card-post-count/
              artalk.pug
              disqus.pug
              fb.pug
              index.pug
              remark42.pug
              twikoo.pug
              valine.pug
              waline.pug
            chat/
              chatra.pug
              crisp.pug
              index.pug
              tidio.pug
            comments/
              artalk.pug
              disqus.pug
              disqusjs.pug
              facebook_comments.pug
              giscus.pug
              gitalk.pug
              index.pug
              js.pug
              livere.pug
              remark42.pug
              twikoo.pug
              utterances.pug
              valine.pug
              waline.pug
            math/
              chartjs.pug
              index.pug
              katex.pug
              mathjax.pug
              mermaid.pug
            newest-comments/
              artalk.pug
              common.pug
              disqus-comment.pug
              github-issues.pug
              index.pug
              remark42.pug
              twikoo-comment.pug
              valine.pug
              waline.pug
            search/
              algolia.pug
              docsearch.pug
              index.pug
              local-search.pug
            share/
              addtoany.pug
              index.pug
              share-js.pug
          widget/
            card_ad.pug
            card_announcement.pug
            card_archives.pug
            card_author.pug
            card_bottom_self.pug
            card_categories.pug
            card_newest_comment.pug
            card_post_series.pug
            card_post_toc.pug
            card_recent_post.pug
            card_tags.pug
            card_top_self.pug
            card_webinfo.pug
            index.pug
      scripts/
        common/
          postDesc.js
        events/
          404.js
          cdn.js
          comment.js
          init.js
          merge_config.js
          stylus.js
          welcome.js
        filters/
          post_lazyload.js
          random_cover.js
          random_cover.js.bak
        helpers/
          aside_archives.js
          aside_categories.js
          getArchiveLength.js
          inject_head_js.js
          page.js
          related_post.js
          series.js
        tag/
          button.js
          chartjs.js
          flink.js
          gallery.js
          hide.js
          inlineImg.js
          label.js
          mermaid.js
          note.js
          score.js
          series.js
          tabs.js
          timeline.js
      source/
        css/
          index.styl
          var.styl
          _global/
            function.styl
            index.styl
          _highlight/
            highlight.styl
            theme.styl
            highlight/
              diff.styl
              index.styl
            prismjs/
              diff.styl
              index.styl
              line-number.styl
          _layout/
            aside.styl
            chat.styl
            comments.styl
            footer.styl
            head.styl
            loading.styl
            pagination.styl
            post.styl
            relatedposts.styl
            reward.styl
            rightside.styl
            sidebar.styl
            third-party.styl
          _mode/
            darkmode.styl
            readmode.styl
          _page/
            404.styl
            archives.styl
            categories.styl
            common.styl
            flink.styl
            homepage.styl
            shuoshuo.styl
            tags.styl
          _search/
            algolia.styl
            index.styl
            local-search.styl
          _tags/
            button.styl
            gallery.styl
            hexo.styl
            hide.styl
            inlineImg.styl
            label.styl
            note.styl
            series.styl
            tabs.styl
            timeline.styl
          _third-party/
            normalize.min.css
        img/
        js/
          main.js
          tw_cn.js
          utils.js
          search/
            algolia.js
            local-search.js
```

## 2. File Contents

### 文件路径: `.gitignore`
```
.DS_Store
Thumbs.db
db.json
*.log
node_modules/
public/
.deploy*/
_multiconfig.yml
```

### 文件路径: `.gitmodules`
```
[submodule "themes/themes/butterfly"]
	path = themes/themes/butterfly
	url = https://github.com/jerryc127/hexo-theme-butterfly.git

```

### 文件路径: `_config.butterfly.yml`
```yml
# --------------------------------------
# Hexo Butterfly Theme Configuration
# If you have any questions, please refer to the documentation
# Chinese: https://butterfly.js.org/
# English: https://butterfly.js.org/en/
# --------------------------------------

# --------------------------------------
# Navigation Settings
# --------------------------------------

nav:
  # Navigation bar logo image
  logo:
  display_title: true
  # Whether to fix navigation bar
  fixed: false

menu:
  # Home: / || fas fa-home
  # List||fas fa-list:
  #   Music: /music/ || fas fa-music
  #   Movie: /movies/ || fas fa-video

# --------------------------------------
# Code Blocks Settings
# --------------------------------------

code_blocks:
  # Code block theme: darker / pale night / light / ocean / false
  theme: light
  macStyle: true
  # Code block height limit (unit: px)
  height_limit: false
  word_wrap: false

  # Toolbar
  copy: true
  language: true
  # true: shrink the code blocks | false: expand the code blocks | none: expand code blocks and hide the button
  shrink: false
  fullpage: false

# Social media links
# Formal:
#   icon: link || the description || color
social:
  # fab fa-github: https://github.com/xxxxx || Github || '#24292e'
  # fas fa-envelope: mailto:xxxxxx@gmail.com || Email || '#4a7dbe'

# --------------------------------------
# Image Settings
# --------------------------------------

favicon: /img/favicon.png

avatar:
  img: /img/butterfly-icon.png
  effect: false

# Disable all banner images
disable_top_img: false

# If the banner of page not setting, it will show the default_top_img
default_top_img:

# The banner image of index page
index_img:

# The banner image of archive page
archive_img:

# Note: tag page, not tags page
tag_img:

# The banner image of tag page, you can set the banner image for each tag
# Format:
#  - tag name: xxxxx
tag_per_img:

# Note: category page, not categories page
category_img:

# The banner image of category page, you can set the banner image for each category
# Format:
#  - category name: xxxxx
category_per_img:

# The background image of footer
footer_img: https://vip.123pan.cn/1813724027/%E8%A7%86%E9%A2%91/%E5%9B%BE%E5%BA%8A/1757768140.jpg

# Website Background
# Can set it to color or image url
background: https://vip.123pan.cn/1813724027/%E8%A7%86%E9%A2%91/%E5%9B%BE%E5%BA%8A/1757768140.jpg

cover:
  # Disable the cover or not
  index_enable: true
  aside_enable: true
  archives_enable: true
  # When cover is not set, the default cover is displayed
  default_cover:
    # - xxx.jpg

# Replace Broken Images
error_img:
  flink: /img/friend_404.gif
  post_page: /img/404.jpg

# A simple 404 page
error_404:
  enable: false
  subtitle: 'Page Not Found'
  background: /img/error-page.png

post_meta:
  # Home Page
  page:
    # Choose: created / updated / both
    date_type: created
    # Choose: date / relative
    date_format: date
    categories: true
    tags: false
    label: true
  post:
    # Choose: left / center
    position: left
    # Choose: created / updated / both
    date_type: both
    # Choose: date / relative
    date_format: date
    categories: true
    tags: true
    label: true

# --------------------------------------
# Index page settings
# --------------------------------------

# The top_img settings of home page
# default: top img - full screen, site info - middle
# The position of site info, eg: 300px/300em/300rem/10%
index_site_info_top:
# The height of top_img, eg: 300px/300em/300rem
index_top_img_height:

# The subtitle on homepage
subtitle:
  enable: false
  # Typewriter Effect
  effect: true
  # Customize typed.js
  # https://github.com/mattboldt/typed.js/#customization
  typed_option:
  # Source - Call the third-party service API (Chinese only)
  # It will show the source first, then show the content of sub
  # Choose: false/1/2/3
  # false - disable the function
  # 1 - hitokoto.cn
  # 2 - yijuzhan.com
  # 3 - jinrishici.com
  source: false
  # If you close the typewriter effect, the subtitle will only show the first line of sub
  sub:

# Article layout on the homepage
# 1: Cover on the left, info on the right
# 2: Cover on the right, info on the left
# 3: Cover and info alternate between left and right
# 4: Cover on top, info on the bottom
# 5: Info displayed on the cover
# 6: Masonry layout - Cover on top, info on the bottom
# 7: Masonry layout - Info displayed on the cover
index_layout: 7

# Display the article introduction on homepage
# 1: description
# 2: both (if the description exists, it will show description, or show the auto_excerpt)
# 3: auto_excerpt (default)
# false: do not show the article introduction
index_post_content:
  method: 3
  # If you set method to 2 or 3, the length need to config
  length: 500

# --------------------------------------
# Post Settings
# --------------------------------------

toc:
  post: true
  page: false
  number: true
  expand: false
  # Only for post
  style_simple: false
  scroll_percent: true

post_copyright:
  enable: true
  decode: false
  author_href:
  license: CC BY-NC-SA 4.0
  license_url: https://creativecommons.org/licenses/by-nc-sa/4.0/

# Sponsor/reward
reward:
  enable: false
  text:
  QR_code:
    # - img: /img/wechat.jpg
    #   link:
    #   text: wechat
    # - img: /img/alipay.jpg
    #   link:
    #   text: alipay

# Post edit
# Easily browse and edit blog source code online.
post_edit:
  enable: false
  # url: https://github.com/user-name/repo-name/edit/branch-name/subdirectory-name/
  # For example: https://github.com/jerryc127/butterfly.js.org/edit/main/source/
  url:

# Related Articles
related_post:
  enable: true
  # Number of posts displayed
  limit: 6
  # Choose: created / updated
  date_type: created

# Choose: 1 / 2 / false
# 1: The 'next post' will link to old post
# 2: The 'next post' will link to new post
# false: disable pagination
post_pagination: 1

# Displays outdated notice for a post
noticeOutdate:
  enable: false
  # Style: simple / flat
  style: flat
  # When will it be shown
  limit_day: 365
  # Position: top / bottom
  position: top
  message_prev: It has been
  message_next: days since the last update, the content of the article may be outdated.

# --------------------------------------
# Footer Settings
footer:
  owner:
    enable: true
    since: 2019
  custom_text: |
    <p>
      <span class="badge-subject"><i class="fa fa-id-card"></i> 尝试呢 </span>
      <span class="badge-value bg-orange">
        <a href="https://www.540601.xyz" target="_blank" rel="noopener">萌ICP备202466666号-1</a> |
        <a href="https://www.540601.xyz" target="_blank" rel="noopener">泪目了</a>
      </span>
    </p>
# --------------------------------------

  # Copyright of theme and framework
  copyright: true

# --------------------------------------
# Aside Settings
# --------------------------------------

aside:
  enable: true
  hide: false
  # Show the button to hide the aside in bottom right button
  button: true
  mobile: true
  # Position: left / right
  position: right
  display:
    archive: true
    tag: true
    category: true
  card_author:
    enable: true
    description:
    button:
      enable: true
      icon: fa-brands fa-bilibili
      text: 关注我的B站不迷路
      link: https://b23.tv/IDADCCS
  card_announcement:
    enable: true
    content: This is my Blog
  card_recent_post:
    enable: true
    # If set 0 will show all
    limit: 5
    # Sort: date / updated
    sort: date
    sort_order:
  card_newest_comments:
    enable: false
    sort_order:
    limit: 6
    # Unit: mins, save data to localStorage
    storage: 10
    avatar: true
  card_categories:
    enable: true
    # If set 0 will show all
    limit: 8
    # Choose: none / true / false
    expand: none
    sort_order:
  card_tags:
    enable: true
    # If set 0 will show all
    limit: 40
    color: false
    # Order of tags, random/name/length
    orderby: random
    # Sort of order. 1, asc for ascending; -1, desc for descending
    order: 1
    sort_order:
  card_archives:
    enable: true
    # Type: monthly / yearly
    type: monthly
    # Eg: YYYY年MM月
    format: MMMM YYYY
    # Sort of order. 1, asc for ascending; -1, desc for descending
    order: -1
    # If set 0 will show all
    limit: 8
    sort_order:
  card_post_series:
    enable: true
    # The title shows the series name
    series_title: false
    # Order by title or date
    orderBy: 'date'
    # Sort of order. 1, asc for ascending; -1, desc for descending
    order: -1
  card_webinfo:
    enable: true
    post_count: true
    last_push_date: true
    sort_order:
    # Time difference between publish date and now
    # Formal: Month/Day/Year Time or Year/Month/Day Time
    # Leave it empty if you don't enable this feature
    runtime_date:

# --------------------------------------
# Bottom right button
# --------------------------------------

# The distance between the bottom right button and the bottom (default unit: px)
rightside_bottom:

# Conversion between Traditional and Simplified Chinese
translate:
  enable: false
  # The text of a button
  default: 繁
  # the language of website (1 - Traditional Chinese/ 2 - Simplified Chinese）
  defaultEncoding: 2
  # Time delay
  translateDelay: 0
  # The text of the button when the language is Simplified Chinese
  msgToTraditionalChinese: '繁'
  # The text of the button when the language is Traditional Chinese
  msgToSimplifiedChinese: '簡'

# Read Mode
readmode: true

# Dark Mode
darkmode:
  enable: true
  # Toggle Button to switch dark/light mode
  button: true
  # Switch dark/light mode automatically
  # autoChangeMode: 1  Following System Settings, if the system doesn't support dark mode, it will switch dark mode between 6 pm to 6 am
  # autoChangeMode: 2  Switch dark mode between 6 pm to 6 am
  # autoChangeMode: false
  autoChangeMode: false
  # Set the light mode time. The value is between 0 and 24. If not set, the default value is 6 and 18
  start:
  end:

# Show scroll percent in scroll-to-top button
rightside_scroll_percent: false

# Don't modify the following settings unless you know how they work
# Choose: readmode,translate,darkmode,hideAside,toc,chat,comment
# Don't repeat the same value
rightside_item_order:
  enable: false
  # Default: readmode,translate,darkmode,hideAside
  hide:
  # Default: toc,chat,comment
  show:

# --------------------------------------
# Global Settings
# --------------------------------------

anchor:
  # When you scroll, the URL will update according to header id.
  auto_update: false
  # Click the headline to scroll and update the anchor
  click_to_scroll: false

photofigcaption: false

copy:
  enable: true
  # Add the copyright information after copied content
  copyright:
    enable: false
    limit_count: 150

# Need to install the hexo-wordcount plugin
wordcount:
  enable: false
  # Display the word count of the article in post meta
  post_wordcount: true
  # Display the time to read the article in post meta
  min2read: true
  # Display the total word count of the website in aside's webinfo
  total_wordcount: true

# Busuanzi count for PV / UV in site
busuanzi:
  site_uv: true
  site_pv: true
  page_pv: true

# --------------------------------------
# Math
# --------------------------------------

# About the per_page
# if you set it to true, it will load mathjax/katex script in each page
# if you set it to false, it will load mathjax/katex script according to your setting (add the 'mathjax: true' or 'katex: true' in page's front-matter)
math:
  # Choose: mathjax, katex
  # Leave it empty if you don't need math
  use:
  per_page: true
  hide_scrollbar: false

  mathjax:
    # Enable the contextual menu
    enableMenu: true
    # Choose: all / ams / none, This controls whether equations are numbered and how
    tags: none

  katex:
    # Enable the copy KaTeX formula
    copy_tex: false

# --------------------------------------
# Search
# --------------------------------------

search:
  # Choose: algolia_search / local_search / docsearch
  # leave it empty if you don't need search
  use: 
  placeholder: 

  # Algolia Search
  algolia_search:
    # Number of search results per page
    hitsPerPage: 6

  # Local Search
  local_search:
    # Preload the search data when the page loads.
    preload: false
    # Show top n results per article, show all results by setting to -1
    top_n_per_article: 1
    # Unescape html strings to the readable one.
    unescape: false
    CDN:

  # Docsearch
  # https://docsearch.algolia.com/
  docsearch:
    appId:
    apiKey:
    indexName:
    option:

# --------------------------------------
# Share System
# --------------------------------------

share:
  # Choose: sharejs / addtoany
  # Leave it empty if you don't need share
  use: sharejs

  # Share.js
  # https://github.com/overtrue/share.js
  sharejs:
    sites: facebook,twitter,wechat,weibo,qq

  # AddToAny
  # https://www.addtoany.com/
  addtoany:
    item: facebook,twitter,wechat,sina_weibo,facebook_messenger,email,copy_link

# --------------------------------------
# Comments System
# --------------------------------------

comments:
  # Up to two comments system, the first will be shown as default
  # Leave it empty if you don't need comments
  # Choose: Disqus/Disqusjs/Livere/Gitalk/Valine/Waline/Utterances/Facebook Comments/Twikoo/Giscus/Remark42/Artalk
  # Format of two comments system : Disqus,Waline
  use: waline
  # Display the comment name next to the button
  text: true
  # Lazyload: The comment system will be load when comment element enters the browser's viewport.
  # If you set it to true, the comment count will be invalid
  lazyload: false
  # Display comment count in post's top_img
  count: false
  # Display comment count in Home Page
  card_post_count: false

# Disqus
# https://disqus.com/
disqus:
  shortname:
  # For newest comments widget
  apikey:

# Alternative Disqus - Render comments with Disqus API
# https://github.com/SukkaW/DisqusJS
disqusjs:
  shortname:
  apikey:
  option:

# Livere
# https://www.livere.com/
livere:
  uid:

# Gitalk
# https://github.com/gitalk/gitalk
gitalk:
  client_id:
  client_secret:
  repo:
  owner:
  admin:
  option:

# Valine
# https://valine.js.org
valine:
  appId:
  appKey:
  avatar: monsterid
  # This configuration is suitable for domestic custom domain name users, overseas version will be automatically detected (no need to manually fill in)
  serverURLs:
  bg:
  # Use Valine visitor count as the page view count
  visitor: false
  option:

# Waline - A simple comment system with backend support fork from Valine
# https://waline.js.org/
waline:
  serverURL: https://pl.zyfytt.top
  bg:
  # Use Waline pageview count as the page view count
  pageview: true
  option:

# Utterances
# https://utteranc.es/
utterances:
  repo:
  # Issue Mapping: pathname/url/title/og:title
  issue_term: pathname
  # Theme: github-light/github-dark/github-dark-orange/icy-dark/dark-blue/photon-dark
  light_theme: github-light
  dark_theme: photon-dark
  js:
  option:

# Facebook Comments Plugin
# https://developers.facebook.com/docs/plugins/comments/
facebook_comments:
  app_id:
  # optional
  user_id:
  pageSize: 10
  # Choose: social / time / reverse_time
  order_by: social
  lang: en_US

# Twikoo
# https://github.com/imaegoo/twikoo
twikoo:
  envId:
  region:
  # Use Twikoo visitor count as the page view count
  visitor: false
  option:

# Giscus
# https://giscus.app/
giscus:
  repo:
  repo_id:
  category_id:
  light_theme: light
  dark_theme: dark
  js:
  option:

# Remark42
# https://remark42.com/docs/configuration/frontend/
remark42:
  host:
  siteId:
  option:

# Artalk
# https://artalk.js.org/guide/frontend/config.html
artalk:
  server:
  site:
  # Use Artalk visitor count as the page view count
  visitor: false
  option:

# --------------------------------------
# Chat Services
# --------------------------------------

chat:
  # Choose: chatra/tidio/crisp
  # Leave it empty if you don't need chat
  use:
  # Chat Button [recommend]
  # It will create a button in the bottom right corner of website, and hide the origin button
  rightside_button: false
  # The origin chat button is displayed when scrolling up, and the button is hidden when scrolling down
  button_hide_show: false

# https://chatra.io/
chatra:
  id:

# https://www.tidio.com/
tidio:
  public_key:

# https://crisp.chat/en/
crisp:
  website_id:

# --------------------------------------
# Analysis
# --------------------------------------

# https://tongji.baidu.com/web/welcome/login
baidu_analytics:

# https://analytics.google.com/analytics/web/
google_analytics:

# https://www.cloudflare.com/zh-tw/web-analytics/
cloudflare_analytics:

# https://clarity.microsoft.com/
microsoft_clarity:

# https://umami.is/
umami_analytics:
  enable: false
  # For self-hosted setups, configure the hostname of the Umami instance
  serverURL:
  website_id:
  option:
  UV_PV:
    site_uv: false
    site_pv: false
    page_pv: false
    # Umami Cloud (API key) / self-hosted Umami (token)
    token:

# --------------------------------------
# Advertisement
# --------------------------------------

# Google Adsense
google_adsense:
  enable: true
  auto_ads: true
  js: https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js
  client:
  enable_page_level_ads: true

# Insert ads manually
# Leave it empty if you don't need ads
ad:
  # Insert ads in the index (every three posts)
  index:
  # Insert ads in aside
  aside:
  # Insert ads in the post (before pagination)
  post:

# --------------------------------------
# Verification
# --------------------------------------

site_verification:
  # - name: google-site-verification
  #   content: xxxxxx
  # - name: baidu-site-verification
  #   content: xxxxxxx

# --------------------------------------
# Beautify / Effect
# --------------------------------------

# Theme color for customize
# Notice: color value must in double quotes like "#000" or may cause error!

# theme_color:
#   enable: true
#   main: "#49B1F5"
#   paginator: "#00c4b6"
#   button_hover: "#FF7242"
#   text_selection: "#00c4b6"
#   link_color: "#99a9bf"
#   meta_color: "#858585"
#   hr_color: "#A4D8FA"
#   code_foreground: "#F47466"
#   code_background: "rgba(27, 31, 35, .05)"
#   toc_color: "#00c4b6"
#   blockquote_padding_color: "#49b1f5"
#   blockquote_background_color: "#49b1f5"
#   scrollbar_color: "#49b1f5"
#   meta_theme_color_light: "ffffff"
#   meta_theme_color_dark: "#0d0d0d"

# The user interface setting of category and tag page
# Choose: index - same as Homepage UI / default - same as archives UI
# leave it empty or index
category_ui:
tag_ui:

# Rounded corners for UI elements
rounded_corners_ui: true

# Stretches the lines so that each line has equal width
text_align_justify: false

# Add a mask to the header and footer
mask:
  header: true
  footer: true

# Loading Animation
preloader:
  enable: false
  # source
  # 1. fullpage-loading
  # 2. pace (progress bar)
  source: 1
  # pace theme (see https://codebyzach.github.io/pace/)
  pace_css_url:

# Page Transition
enter_transitions: true

# Default display mode - light (default) / dark
display_mode: light

# Configuration for beautifying the content of the article
beautify:
  enable: true
  # Specify the field to beautify (site or post)
  field: post
  # Specify the icon to be used as a prefix for the title, such as '\f0c1'
  title_prefix_icon: 
  # Specify the color of the title prefix icon, such as '#F47466'
  title_prefix_icon_color:

# Global font settings
# Don't modify the following settings unless you know how they work
font:
  global_font_size:
  code_font_size:
  font_family:
  code_font_family:

# Font settings for the site title and site subtitle
blog_title_font:
  font_link:
  font_family:

# The setting of divider icon
hr_icon:
  enable: true
  # The unicode value of Font Awesome icon, such as '\3423'
  icon:
  icon_top:

# Typewriter Effect
# https://github.com/disjukr/activate-power-mode
activate_power_mode:
  enable: false
  colorful: true
  shake: true
  mobile: false

# Background effects
# --------------------------------------

# canvas_ribbon
# See: https://github.com/hustcc/ribbon.js
canvas_ribbon:
  enable: true
  # The size of ribbon
  size: 150
  # The opacity of ribbon (0 ~ 1)
  alpha: 0.6
  zIndex: -1
  click_to_change: true
  mobile: true

# Fluttering Ribbon
canvas_fluttering_ribbon:
  enable: false
  mobile: false

# canvas_nest
# https://github.com/hustcc/canvas-nest.js
canvas_nest:
  enable: false
  # Color of lines, default: '0,0,0'; RGB values: (R,G,B).(note: use ',' to separate.)
  color: '0,0,255'
  # The opacity of line (0~1)
  opacity: 0.7
  # The z-index property of the background
  zIndex: -1
  # The number of lines
  count: 99
  mobile: false

# Mouse click effects: fireworks
fireworks:
  enable: false
  zIndex: 9999
  mobile: false

# Mouse click effects: Heart symbol
click_heart:
  enable: false
  mobile: false

# Mouse click effects: words
clickShowText:
  enable: false
  text:
    # - I
    # - LOVE
    # - YOU
  fontSize: 15px
  random: false
  mobile: false

# --------------------------------------
# Lightbox Settings
# --------------------------------------

# Choose: fancybox / medium_zoom
# https://github.com/francoischalifour/medium-zoom
# https://fancyapps.com/fancybox/
# Leave it empty if you don't need lightbox
lightbox:

# --------------------------------------
# Tag Plugins settings
# --------------------------------------

# Series
series:
  enable: false
  # Order by title or date
  orderBy: 'title'
  # Sort of order. 1, asc for ascending; -1, desc for descending
  order: 1
  number: true

# ABCJS - The ABC Music Notation Plugin
# https://github.com/paulrosen/abcjs
abcjs:
  enable: false
  per_page: true

# Mermaid
# https://github.com/mermaid-js/mermaid
mermaid:
  enable: false
  # Write Mermaid diagrams using code blocks
  code_write: false
  # built-in themes: default / forest / dark / neutral
  theme:
    light: default
    dark: dark

# chartjs
# see https://www.chartjs.org/docs/latest/
chartjs:
  enable: false
  # Do not modify unless you understand how they work.
  # The default settings are only used when the MD syntax is not specified.
  # General font color for the chart
  fontColor:
    light: 'rgba(0, 0, 0, 0.8)'
    dark: 'rgba(255, 255, 255, 0.8)'
  # General border color for the chart
  borderColor:
    light: 'rgba(0, 0, 0, 0.1)'
    dark: 'rgba(255, 255, 255, 0.2)'
  # Background color for scale labels on radar and polar area charts
  scale_ticks_backdropColor:
    light: 'transparent'
    dark: 'transparent'

# Note - Bootstrap Callout
note:
  # Note tag style values:
  #  - simple    bs-callout old alert style. Default.
  #  - modern    bs-callout new (v2-v3) alert style.
  #  - flat      flat callout style with background, like on Mozilla or StackOverflow.
  #  - disabled  disable all CSS styles import of note tag.
  style: flat
  icons: true
  border_radius: 3
  # Offset lighter of background in % for modern and flat styles (modern: -12 | 12; flat: -18 | 6).
  # Offset also applied to label tag variables. This option can work with disabled note tag.
  light_bg_offset: 0

# --------------------------------------
# Other Settings
# --------------------------------------

# https://github.com/MoOx/pjax
pjax:
  enable: false
  # Exclude the specified pages from pjax, such as '/music/'
  exclude:
    # - /xxxxxx/

# Inject the css and script (aplayer/meting)
aplayerInject:
  enable: false
  per_page: true

# Snackbar - Toast Notification
# https://github.com/polonel/SnackBar
# position: top-left / top-center / top-right / bottom-left / bottom-center / bottom-right
snackbar:
  enable: false
  position: bottom-left
  # The background color of Toast Notification in light mode and dark mode
  bg_light: '#49b1f5'
  bg_dark: '#1f1f1f'

# Instant.page
# https://instant.page/
instantpage: false

# Lazyload
# https://github.com/verlok/vanilla-lazyload
lazyload:
  enable: false
  # Specify the field to use lazyload (site or post)
  field: site
  placeholder:
  blur: false

# PWA
# See https://github.com/JLHwung/hexo-offline
# ---------------
pwa:
  enable: false
  manifest:
  apple_touch_icon:
  favicon_32_32:
  favicon_16_16:
  mask_icon:

# Open graph meta tags
# https://hexo.io/docs/helpers#open-graph
Open_Graph_meta:
  enable: true
  option:
    # twitter_card:
    # twitter_image:
    # twitter_id:
    # twitter_site:
    # google_plus:
    # fb_admins:
    # fb_app_id:

# Structured Data
# https://developers.google.com/search/docs/guides/intro-structured-data
structured_data: true

# Add the vendor prefixes to ensure compatibility
css_prefix: true

# Inject
# Insert the code to head (before '</head>' tag) and the bottom (before '</body>' tag)
inject:
  head:
    # - <link rel="stylesheet" href="/xxx.css">
  bottom:
    # - <script src="xxxx"></script>

# CDN Settings
# Don't modify the following settings unless you know how they work
CDN:
  # The CDN provider for internal and third-party scripts
  # Options for both: local/jsdelivr/unpkg/cdnjs/custom
  # Note: Dev version can only use 'local' for internal scripts
  # Note: When setting third-party scripts to 'local', you need to install hexo-butterfly-extjs
  internal_provider: local
  third_party_provider: jsdelivr

  # Add version number to url, true or false
  version: false

  # Custom format
  # For example: https://cdn.staticfile.org/${cdnjs_name}/${version}/${min_cdnjs_file}
  custom_format:

  option:
    # abcjs_basic_js:
    # activate_power_mode:
    # algolia_js:
    # algolia_search:
    # aplayer_css:
    # aplayer_js:
    # artalk_css:
    # artalk_js:
    # blueimp_md5:
    # busuanzi:
    # canvas_fluttering_ribbon:
    # canvas_nest:
    # canvas_ribbon:
    # chartjs:
    # click_heart:
    # clickShowText:
    # disqusjs:
    # disqusjs_css:
    # docsearch_css:
    # docsearch_js:
    # egjs_infinitegrid:
    # fancybox:
    # fancybox_css:
    # fireworks:
    # fontawesome:
    # gitalk:
    # gitalk_css:
    # giscus:
    # instantpage:
    # instantsearch:
    # katex:
    # katex_copytex:
    # lazyload:
    # local_search:
    # main:
    # main_css:
    # mathjax:
    # medium_zoom:
    # mermaid:
    # meting_js:
    # prismjs_autoloader:
    # prismjs_js:
    # prismjs_lineNumber_js:
    # pjax:
    # sharejs:
    # sharejs_css:
    # snackbar:
    # snackbar_css:
    # translate:
    # twikoo:
    # typed:
    # utils:
    # valine:
    # waline_css:
    # waline_js:

```

### 文件路径: `_config.yml`
```yml
# Hexo Configuration
## Docs: https://hexo.io/docs/configuration.html
## Source: https://github.com/hexojs/hexo/

# Site
title: 同天の博客
subtitle: '看到我你会幸运'
description: '这是风月同天的个人博客'
keywords:
author: 风月同天
language: zh-CN
timezone: 'Asia/Shanghai'

# URL
## Set your site url here. For example, if you use GitHub Page, set url as 'https://username.github.io/project'
url: https://www.540601.xyz
permalink: :abbrlink/
permalink_defaults:
pretty_urls:
  trailing_index: false # Set to false to remove trailing 'index.html' from permalinks
  trailing_html: false # Set to false to remove trailing '.html' from permalinks

# Directory
source_dir: source
public_dir: public
tag_dir: tags
archive_dir: archives
category_dir: categories
code_dir: downloads/code
i18n_dir: :lang
skip_render:

# Writing
new_post_name: :title.md # File name of new posts
default_layout: post
titlecase: false # Transform title into titlecase
external_link:
  enable: true # Open external links in new tab
  field: site # Apply to the whole site
  exclude: ''
filename_case: 0
render_drafts: false
post_asset_folder: true
relative_link: false
future: true
syntax_highlighter: highlight.js
highlight:
  line_number: true
  auto_detect: false
  tab_replace: ''
  wrap: true
  hljs: false
prismjs:
  preprocess: true
  line_number: true
  tab_replace: ''

# Home page setting
# path: Root path for your blogs index page. (default = '')
# per_page: Posts displayed per page. (0 = disable pagination)
# order_by: Posts order. (Order by date descending by default)
index_generator:
  path: ''
  per_page: 10
  order_by: -date

# Category & Tag
default_category: uncategorized
category_map:
tag_map:

# Metadata elements
## https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meta
meta_generator: true

# Date / Time format
## Hexo uses Moment.js to parse and display date
## You can customize the date format as defined in
## http://momentjs.com/docs/#/displaying/format/
date_format: YYYY-MM-DD
time_format: HH:mm:ss
## updated_option supports 'mtime', 'date', 'empty'
updated_option: 'mtime'

# Pagination
## Set per_page to 0 to disable pagination
per_page: 10
pagination_dir: page

# Include / Exclude file(s)
## include:/exclude: options only apply to the 'source/' folder
include:
exclude:
ignore:

# Extensions
## Plugins: https://hexo.io/plugins/
## Themes: https://hexo.io/themes/
theme: butterfly

# Deployment
## Docs: https://hexo.io/docs/one-command-deployment
deploy:
  type: git
  repo: git@github.com:ZZ0YY/hexo-starter.git  # SSH 地址
  branch: main  # 确保与你的 GitHub 仓库默认分支一致（通常是 main）


# abbrlink config
## https://github.com/rozbo/hexo-abbrlink
abbrlink:
  alg: crc32 # support crc16(default) and crc32
  rep: hex # support dec(default) and hex
  drafts: false # (true)Process draft,(false)Do not process draft. false(default)
  # Generate categories from directory-tree
  # depth: the max_depth of directory-tree you want to generate, should > 0
  auto_category:
     enable: true # true(default)
     depth: 3 # 3(default)
     over_write: false
  auto_title: false # enable auto title, it can auto fill the title by path
  auto_date: false # enable auto date, it can auto fill the date by time today
  force: true # enable force mode, in this mode, the plugin will ignore the cache, and calc the abbrlink for every post even it already had abbrlink.
  seed: 123456     # 固定种子值
  lower: true

# hexo-generator-sitemap
## https://github.com/hexojs/hexo-generator-sitemap
sitemap:
  path: sitemap.xml
  # template: ./sitemap_template.xml
  rel: true
  tags: false
  categories: false

nofollow:
  enable: true
  field: site
  exclude:
    - 'www.540601.xyz'

marked:
  gfm: true
  pedantic: false
  breaks: true
  smartLists: true
  smartypants: true
  quotes: '“”‘’'
  modifyAnchors: 0
  anchorAlias: false
  autolink: true
  mangle: true
  sanitizeUrl: false
  dompurify: false
  headerIds: true
  lazyload: false
  figcaption: false
  prependRoot: true
  postAsset: true
  external_link:
    enable: false
    exclude: []
    nofollow: false
  disableNunjucks: false
  descriptionLists: true
```

### 文件路径: `package.json`
```json
{
  "name": "hexo-site",
  "version": "0.0.0",
  "private": true,
  "scripts": {
    "build": "hexo clean && hexo generate",
    "clean": "hexo clean",
    "deploy": "hexo deploy",
    "server": "hexo server"
  },
  "hexo": {
    "version": "7.3.0"
  },
  "dependencies": {
    "hexo": "^7.3.0",
    "hexo-abbrlink": "^2.2.1",
    "hexo-deployer-git": "^4.0.0",
    "hexo-filter-nofollow": "^2.0.2",
    "hexo-generator-archive": "^2.0.0",
    "hexo-generator-category": "^2.0.0",
    "hexo-generator-index": "^4.0.0",
    "hexo-generator-sitemap": "^3.0.1",
    "hexo-generator-tag": "^2.0.0",
    "hexo-renderer-ejs": "^2.0.0",
    "hexo-renderer-marked": "^7.0.0",
    "hexo-renderer-stylus": "^3.0.1",
    "hexo-server": "^3.0.0",
    "hexo-theme-butterfly": "^5.4.2",
    "hexo-theme-landscape": "^1.0.0"
  }
}

```

### 文件路径: `.github\dependabot.yml`
```yml
version: 2
updates:
- package-ecosystem: npm
  directory: "/"
  schedule:
    interval: daily
  open-pull-requests-limit: 20

```

### 文件路径: `scaffolds\draft.md`
```md
---
title: {{ title }}
tags:
---

```

### 文件路径: `scaffolds\page.md`
```md
---
title: {{ title }}
date: {{ date }}
---

```

### 文件路径: `scaffolds\post.md`
```md

```

### 文件路径: `scaffolds\post.md.bak`
```bak
---
title: {{ title }}
date: {{ date }}
tags:
---

```

### 文件路径: `themes\.gitkeep`
```

```

### 文件路径: `themes\butterfly\.gitignore`
```
.DS_Store
.DS_Store

```

### 文件路径: `themes\butterfly\LICENSE`
```

                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright [yyyy] [name of copyright owner]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
```

### 文件路径: `themes\butterfly\README.md`
```md
<div align="right">
<a title="Chinese" href="/README_CN.md">中文</a>
</div>

<div align="center">

<img src="./source/img/butterfly-icon.png" width="150" height="150" />

# hexo-theme-butterfly

![master version](https://img.shields.io/github/package-json/v/jerryc127/hexo-theme-butterfly/master?color=%231ab1ad&label=master)
![master version](https://img.shields.io/github/package-json/v/jerryc127/hexo-theme-butterfly/dev?label=dev)
![https://img.shields.io/npm/v/hexo-theme-butterfly?color=%09%23bf00ff](https://img.shields.io/npm/v/hexo-theme-butterfly?color=%09%23bf00ff)
![hexo version](https://img.shields.io/badge/hexo-5.3.0+-0e83c)
![license](https://img.shields.io/github/license/jerryc127/hexo-theme-butterfly?color=FF5531)

📢 Demo: [Butterfly](https://butterfly.js.org/) / [CrazyWong](https://blog.crazywong.com/)

📖 Docs: [English](https://butterfly.js.org/en/posts/butterfly-docs-en-get-started/) / [Chinese](https://butterfly.js.org/posts/21cfbf15/)

![](https://cdn.jsdelivr.net/gh/jerryc127/CDN@m2/img/theme-butterfly-readme.png)

</div>

---

## 💻 Installation

### GIT

> If you are in Mainland China, you can download in [Gitee](https://gitee.com/immyw/hexo-theme-butterfly.git)

Stable branch [recommend]:

```
git clone -b master https://github.com/jerryc127/hexo-theme-butterfly.git themes/butterfly
```

Dev branch:

```
git clone -b dev https://github.com/jerryc127/hexo-theme-butterfly.git themes/butterfly
```

### NPM

> It supports Hexo 5.0.0 or later

In Hexo site root directory 

```powershell
npm i hexo-theme-butterfly
```

## ⚙ Configuration

 Set theme in the hexo work folder's root config file `_config.yml`: 

> theme: butterfly

 If you don't have pug & stylus renderer, try this: 

> npm install hexo-renderer-pug hexo-renderer-stylus

## 🎉 Features

- [x] Card UI Design
- [x] Rounded Design/Squared Design
- [X] Support sub-menu
- [x] Two-column layout
- [x] Responsive Web Design
- [x] Dark Mode
- [x] Pjax
- [x] Read Mode
- [x] Conversion between Traditional and Simplified Chinese
- [X] TOC catalog is available for both computers and mobile phones
- [X] Built-in Syntax Highlighting Themes (darker/pale night/light/ocean), also support customization
- [X] Code Blocks (Display code language/close or expand Code Blocks/Copy Button/word wrap)
- [X] Disable copy/Add a Copyright Notice to the Copied Text
- [X] Search (Algolia Search/Local Search)
- [x] Mathjax and Katex
- [x] Built-in 404 page
- [x] WordCount
- [x] Related articles
- [x] Displays outdated notice for a post
- [x] Share (Sharejs/Addtoany)
- [X] Comment (Disqus/Disqusjs/Livere/Gitalk/Valine/Waline/Utterances/Facebook Comments/Twikoo/Giscus/Remark42/artalk)
- [x] Multiple Comment System Support
- [x] Online Chats (Chatra/Tidio/Crisp)
- [x] Web analytics
- [x] Google AdSense
- [x] Webmaster Verification
- [x] Change website colour scheme
- [x] Typewriter Effect: activate_power_mode
- [x] Background effects (Canvas ribbon/canvas_ribbon_piao/canvas_nest)
- [x] Mouse click effects (Fireworks/Heart/Text)
- [x] Preloader/Loading Animation/pace.js
- [x] Busuanzi visitor counter
- [x] Medium Zoom/Fancybox
- [x] Mermaid
- [x] Chart.js
- [x] Justified Gallery
- [x] Lazyload images
- [x] Instantpage/Snackbar notification toast/PWA......

## ✨ Contributors

<a href="https://github.com/jerryc127/hexo-theme-butterfly/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=jerryc127/hexo-theme-butterfly" />
</a>

## 📷 Screenshots

![](https://cdn.jsdelivr.net/gh/jerryc127/CDN@m2/img/butterfly-readme-screenshots-1.jpg)
![](https://cdn.jsdelivr.net/gh/jerryc127/CDN@m2/img/butterfly-readme-screenshots-2.jpg)
![](https://cdn.jsdelivr.net/gh/jerryc127/CDN@m2/img/butterfly-readme-screenshots-3.jpg)
![](https://cdn.jsdelivr.net/gh/jerryc127/CDN@m2/img/butterfly-readme-screenshots-4.jpg)

```

### 文件路径: `themes\butterfly\README_CN.md`
```md
<div align="right">
  <a title="English" href="/README.md">English</a>
</div>

<div align="center">

<img src="./source/img/butterfly-icon.png" width="150" height="150" />

# hexo-theme-butterfly

![master version](https://img.shields.io/github/package-json/v/jerryc127/hexo-theme-butterfly/master?color=%231ab1ad&label=master)
![master version](https://img.shields.io/github/package-json/v/jerryc127/hexo-theme-butterfly/dev?label=dev)
![https://img.shields.io/npm/v/hexo-theme-butterfly?color=%09%23bf00ff](https://img.shields.io/npm/v/hexo-theme-butterfly?color=%09%23bf00ff)
![hexo version](https://img.shields.io/badge/hexo-5.3.0+-0e83c)
![license](https://img.shields.io/github/license/jerryc127/hexo-theme-butterfly?color=FF5531)

📢 預覽: [Butterfly](https://butterfly.js.org/) / [CrazyWong](https://blog.crazywong.com/)

📖 文檔: [中文](https://butterfly.js.org/posts/21cfbf15/) / [English](https://butterfly.js.org/en/posts/butterfly-docs-en-get-started/)

![](https://cdn.jsdelivr.net/gh/jerryc127/CDN@m2/img/theme-butterfly-readme.png)

</div>

---

## 💻 安裝

### Git 安裝

> 本倉庫同時上傳到 [Gitee](https://gitee.com/immyw/hexo-theme-butterfly.git)，如果你訪問 Github 緩慢，可從 Gitee 中下載。

在博客根目錄裡安裝穩定版【推薦】

```powershell
git clone -b master https://github.com/jerryc127/hexo-theme-butterfly.git themes/butterfly
```

如果想要安裝比較新的dev分支，可以

```powershell
git clone -b dev https://github.com/jerryc127/hexo-theme-butterfly.git themes/butterfly
```

### npm 安裝

> 此方法只支持Hexo 5.0.0以上版本

在博客根目錄裡

```powershell
npm i hexo-theme-butterfly
```

## ⚙ 應用主題

修改hexo配置文件`_config.yml`，把主題改為`Butterfly`

```
theme: butterfly
```

>如果你沒有pug以及stylus的渲染器，請下載安裝： npm install hexo-renderer-pug hexo-renderer-stylus --save

## 🎉 特色

- [x] 卡片化設計
- [x] 圓角化設計/直角化設計
- [X] 支持二級目錄
- [x] 雙欄設計
- [x] 響應式主題
- [x] 夜間模式
- [x] Pjax
- [x] 文章閲讀模式
- [x] 簡體和繁體轉換
- [X] 電腦和手機都可查看TOC目錄
- [X] 內置多種代碼配色（darker/pale night/light/ocean），可自定義代碼配色
- [X] 代碼塊顯示代碼語言/關閉或展開代碼塊/代碼複製/代碼自動換行
- [X] 可關閉文字複製/可開啟內容複製增加版權信息）
- [X] 兩種搜索（ Algolia 搜索和本地搜索）
- [x] Mathjax 和 Katex
- [x] 內置404頁面
- [x] 顯示字數統計
- [x] 顯示相關文章
- [x] 過期文章提醒
- [x] 多種分享系統（Sharejs/Addtoany）
- [X] 多種評論系統（Disqus/Disqusjs/Livere/Gitalk/Valine/Waline/Utterances/Facebook Comments/Twikoo/Giscus/Remark42/artalk）
- [x] 支持雙評論部署
- [x] 多種在線聊天（Chatra/Tidio/Crisp）
- [x] 多種分析系統
- [x] 谷歌廣告/手動廣告位置
- [x] 各種站長驗證
- [x] 修改網站配色
- [x] 打字特效 activate_power_mode
- [x] 多種背景特效（靜止彩帶/動態彩帶/Canvas Nest）
- [x] 多種鼠標點擊特效（煙花/文字/愛心）
- [x] 內置一種 Preloader 加載動畫和 pace.js 加載動畫條
- [x] 不蒜子訪問統計
- [x] 兩種大圖模式（Medium Zoom/Fancybox）
- [x] Mermaid 圖表顯示
- [x] Chart.js 圖表顯示
- [x] 照片牆
- [x] 圖片懶加載
- [x] Instantpage/Snackbar彈窗/PWA......

## ✨ 貢獻者

<a href="https://github.com/jerryc127/hexo-theme-butterfly/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=jerryc127/hexo-theme-butterfly" />
</a>

## 📷 截圖

![](https://cdn.jsdelivr.net/gh/jerryc127/CDN@m2/img/butterfly-readme-screenshots-1.jpg)
![](https://cdn.jsdelivr.net/gh/jerryc127/CDN@m2/img/butterfly-readme-screenshots-2.jpg)
![](https://cdn.jsdelivr.net/gh/jerryc127/CDN@m2/img/butterfly-readme-screenshots-3.jpg)
![](https://cdn.jsdelivr.net/gh/jerryc127/CDN@m2/img/butterfly-readme-screenshots-4.jpg)

```

### 文件路径: `themes\butterfly\_config.yml`
```yml
# --------------------------------------
# Hexo Butterfly Theme Configuration
# If you have any questions, please refer to the documentation
# Chinese: https://butterfly.js.org/
# English: https://butterfly.js.org/en/
# --------------------------------------

# --------------------------------------
# Navigation Settings
# --------------------------------------

nav:
  # Navigation bar logo image
  logo:
  display_title: true
  # Whether to fix navigation bar
  fixed: false

menu:
  # Home: / || fas fa-home
  # List||fas fa-list:
  #   Music: /music/ || fas fa-music
  #   Movie: /movies/ || fas fa-video

# --------------------------------------
# Code Blocks Settings
# --------------------------------------

code_blocks:
  # Code block theme: darker / pale night / light / ocean / false
  theme: light
  macStyle: true
  # Code block height limit (unit: px)
  height_limit: false
  word_wrap: false

  # Toolbar
  copy: true
  language: true
  # true: shrink the code blocks | false: expand the code blocks | none: expand code blocks and hide the button
  shrink: false
  fullpage: false

# Social media links
# Formal:
#   icon: link || the description || color
social:
  # fab fa-github: https://github.com/xxxxx || Github || '#24292e'
  # fas fa-envelope: mailto:xxxxxx@gmail.com || Email || '#4a7dbe'

# --------------------------------------
# Image Settings
# --------------------------------------

favicon: /img/favicon.png

avatar:
  img: /img/butterfly-icon.png
  effect: false

# Disable all banner images
disable_top_img: false

# If the banner of page not setting, it will show the default_top_img
default_top_img:

# The banner image of index page
index_img:

# The banner image of archive page
archive_img:

# Note: tag page, not tags page
tag_img:

# The banner image of tag page, you can set the banner image for each tag
# Format:
#  - tag name: xxxxx
tag_per_img:

# Note: category page, not categories page
category_img:

# The banner image of category page, you can set the banner image for each category
# Format:
#  - category name: xxxxx
category_per_img:

# The background image of footer
footer_img: false

# Website Background
# Can set it to color or image url
background:

cover:
  # Disable the cover or not
  index_enable: true
  aside_enable: true
  archives_enable: true
  # When cover is not set, the default cover is displayed
  default_cover:
    # - xxx.jpg

# Replace Broken Images
error_img:
  flink: /img/friend_404.gif
  post_page: /img/404.jpg

# A simple 404 page
error_404:
  enable: false
  subtitle: 'Page Not Found'
  background: /img/error-page.png

post_meta:
  # Home Page
  page:
    # Choose: created / updated / both
    date_type: created
    # Choose: date / relative
    date_format: date
    categories: true
    tags: false
    label: true
  post:
    # Choose: left / center
    position: left
    # Choose: created / updated / both
    date_type: both
    # Choose: date / relative
    date_format: date
    categories: true
    tags: true
    label: true

# --------------------------------------
# Index page settings
# --------------------------------------

# The top_img settings of home page
# default: top img - full screen, site info - middle
# The position of site info, eg: 300px/300em/300rem/10%
index_site_info_top:
# The height of top_img, eg: 300px/300em/300rem
index_top_img_height:

# The subtitle on homepage
subtitle:
  enable: false
  # Typewriter Effect
  effect: true
  # Customize typed.js
  # https://github.com/mattboldt/typed.js/#customization
  typed_option:
  # Source - Call the third-party service API (Chinese only)
  # It will show the source first, then show the content of sub
  # Choose: false/1/2/3
  # false - disable the function
  # 1 - hitokoto.cn
  # 2 - yijuzhan.com
  # 3 - jinrishici.com
  source: false
  # If you close the typewriter effect, the subtitle will only show the first line of sub
  sub:

# Article layout on the homepage
# 1: Cover on the left, info on the right
# 2: Cover on the right, info on the left
# 3: Cover and info alternate between left and right
# 4: Cover on top, info on the bottom
# 5: Info displayed on the cover
# 6: Masonry layout - Cover on top, info on the bottom
# 7: Masonry layout - Info displayed on the cover
index_layout: 3

# Display the article introduction on homepage
# 1: description
# 2: both (if the description exists, it will show description, or show the auto_excerpt)
# 3: auto_excerpt (default)
# false: do not show the article introduction
index_post_content:
  method: 3
  # If you set method to 2 or 3, the length need to config
  length: 500

# --------------------------------------
# Post Settings
# --------------------------------------

toc:
  post: true
  page: false
  number: true
  expand: false
  # Only for post
  style_simple: false
  scroll_percent: true

post_copyright:
  enable: true
  decode: false
  author_href:
  license: CC BY-NC-SA 4.0
  license_url: https://creativecommons.org/licenses/by-nc-sa/4.0/

# Sponsor/reward
reward:
  enable: false
  text:
  QR_code:
    # - img: /img/wechat.jpg
    #   link:
    #   text: wechat
    # - img: /img/alipay.jpg
    #   link:
    #   text: alipay

# Post edit
# Easily browse and edit blog source code online.
post_edit:
  enable: false
  # url: https://github.com/user-name/repo-name/edit/branch-name/subdirectory-name/
  # For example: https://github.com/jerryc127/butterfly.js.org/edit/main/source/
  url:

# Related Articles
related_post:
  enable: true
  # Number of posts displayed
  limit: 6
  # Choose: created / updated
  date_type: created

# Choose: 1 / 2 / false
# 1: The 'next post' will link to old post
# 2: The 'next post' will link to new post
# false: disable pagination
post_pagination: 1

# Displays outdated notice for a post
noticeOutdate:
  enable: false
  # Style: simple / flat
  style: flat
  # When will it be shown
  limit_day: 365
  # Position: top / bottom
  position: top
  message_prev: It has been
  message_next: days since the last update, the content of the article may be outdated.

# --------------------------------------
# Footer Settings
# --------------------------------------
footer:
  owner:
    enable: true
    since: 2019
  custom_text:
  # Copyright of theme and framework
  copyright: true

# --------------------------------------
# Aside Settings
# --------------------------------------

aside:
  enable: true
  hide: false
  # Show the button to hide the aside in bottom right button
  button: true
  mobile: true
  # Position: left / right
  position: right
  display:
    archive: true
    tag: true
    category: true
  card_author:
    enable: true
    description:
    button:
      enable: true
      icon: fab fa-github
      text: Follow Me
      link: https://github.com/xxxxxx
  card_announcement:
    enable: true
    content: This is my Blog
  card_recent_post:
    enable: true
    # If set 0 will show all
    limit: 5
    # Sort: date / updated
    sort: date
    sort_order:
  card_newest_comments:
    enable: false
    sort_order:
    limit: 6
    # Unit: mins, save data to localStorage
    storage: 10
    avatar: true
  card_categories:
    enable: true
    # If set 0 will show all
    limit: 8
    # Choose: none / true / false
    expand: none
    sort_order:
  card_tags:
    enable: true
    # If set 0 will show all
    limit: 40
    color: false
    # Order of tags, random/name/length
    orderby: random
    # Sort of order. 1, asc for ascending; -1, desc for descending
    order: 1
    sort_order:
  card_archives:
    enable: true
    # Type: monthly / yearly
    type: monthly
    # Eg: YYYY年MM月
    format: MMMM YYYY
    # Sort of order. 1, asc for ascending; -1, desc for descending
    order: -1
    # If set 0 will show all
    limit: 8
    sort_order:
  card_post_series:
    enable: true
    # The title shows the series name
    series_title: false
    # Order by title or date
    orderBy: 'date'
    # Sort of order. 1, asc for ascending; -1, desc for descending
    order: -1
  card_webinfo:
    enable: true
    post_count: true
    last_push_date: true
    sort_order:
    # Time difference between publish date and now
    # Formal: Month/Day/Year Time or Year/Month/Day Time
    # Leave it empty if you don't enable this feature
    runtime_date:

# --------------------------------------
# Bottom right button
# --------------------------------------

# The distance between the bottom right button and the bottom (default unit: px)
rightside_bottom:

# Conversion between Traditional and Simplified Chinese
translate:
  enable: false
  # The text of a button
  default: 繁
  # the language of website (1 - Traditional Chinese/ 2 - Simplified Chinese）
  defaultEncoding: 2
  # Time delay
  translateDelay: 0
  # The text of the button when the language is Simplified Chinese
  msgToTraditionalChinese: '繁'
  # The text of the button when the language is Traditional Chinese
  msgToSimplifiedChinese: '簡'

# Read Mode
readmode: true

# Dark Mode
darkmode:
  enable: true
  # Toggle Button to switch dark/light mode
  button: true
  # Switch dark/light mode automatically
  # autoChangeMode: 1  Following System Settings, if the system doesn't support dark mode, it will switch dark mode between 6 pm to 6 am
  # autoChangeMode: 2  Switch dark mode between 6 pm to 6 am
  # autoChangeMode: false
  autoChangeMode: false
  # Set the light mode time. The value is between 0 and 24. If not set, the default value is 6 and 18
  start:
  end:

# Show scroll percent in scroll-to-top button
rightside_scroll_percent: false

# Don't modify the following settings unless you know how they work
# Choose: readmode,translate,darkmode,hideAside,toc,chat,comment
# Don't repeat the same value
rightside_item_order:
  enable: false
  # Default: readmode,translate,darkmode,hideAside
  hide:
  # Default: toc,chat,comment
  show:

# --------------------------------------
# Global Settings
# --------------------------------------

anchor:
  # When you scroll, the URL will update according to header id.
  auto_update: false
  # Click the headline to scroll and update the anchor
  click_to_scroll: false

photofigcaption: false

copy:
  enable: true
  # Add the copyright information after copied content
  copyright:
    enable: false
    limit_count: 150

# Need to install the hexo-wordcount plugin
wordcount:
  enable: false
  # Display the word count of the article in post meta
  post_wordcount: true
  # Display the time to read the article in post meta
  min2read: true
  # Display the total word count of the website in aside's webinfo
  total_wordcount: true

# Busuanzi count for PV / UV in site
busuanzi:
  site_uv: true
  site_pv: true
  page_pv: true

# --------------------------------------
# Math
# --------------------------------------

# About the per_page
# if you set it to true, it will load mathjax/katex script in each page
# if you set it to false, it will load mathjax/katex script according to your setting (add the 'mathjax: true' or 'katex: true' in page's front-matter)
math:
  # Choose: mathjax, katex
  # Leave it empty if you don't need math
  use:
  per_page: true
  hide_scrollbar: false

  mathjax:
    # Enable the contextual menu
    enableMenu: true
    # Choose: all / ams / none, This controls whether equations are numbered and how
    tags: none

  katex:
    # Enable the copy KaTeX formula
    copy_tex: false

# --------------------------------------
# Search
# --------------------------------------

search:
  # Choose: algolia_search / local_search / docsearch
  # leave it empty if you don't need search
  use:
  placeholder:

  # Algolia Search
  algolia_search:
    # Number of search results per page
    hitsPerPage: 6

  # Local Search
  local_search:
    # Preload the search data when the page loads.
    preload: false
    # Show top n results per article, show all results by setting to -1
    top_n_per_article: 1
    # Unescape html strings to the readable one.
    unescape: false
    CDN:

  # Docsearch
  # https://docsearch.algolia.com/
  docsearch:
    appId:
    apiKey:
    indexName:
    option:

# --------------------------------------
# Share System
# --------------------------------------

share:
  # Choose: sharejs / addtoany
  # Leave it empty if you don't need share
  use: sharejs

  # Share.js
  # https://github.com/overtrue/share.js
  sharejs:
    sites: facebook,twitter,wechat,weibo,qq

  # AddToAny
  # https://www.addtoany.com/
  addtoany:
    item: facebook,twitter,wechat,sina_weibo,facebook_messenger,email,copy_link

# --------------------------------------
# Comments System
# --------------------------------------

comments:
  # Up to two comments system, the first will be shown as default
  # Leave it empty if you don't need comments
  # Choose: Disqus/Disqusjs/Livere/Gitalk/Valine/Waline/Utterances/Facebook Comments/Twikoo/Giscus/Remark42/Artalk
  # Format of two comments system : Disqus,Waline
  use:
  # Display the comment name next to the button
  text: true
  # Lazyload: The comment system will be load when comment element enters the browser's viewport.
  # If you set it to true, the comment count will be invalid
  lazyload: false
  # Display comment count in post's top_img
  count: false
  # Display comment count in Home Page
  card_post_count: false

# Disqus
# https://disqus.com/
disqus:
  shortname:
  # For newest comments widget
  apikey:

# Alternative Disqus - Render comments with Disqus API
# https://github.com/SukkaW/DisqusJS
disqusjs:
  shortname:
  apikey:
  option:

# Livere
# https://www.livere.com/
livere:
  uid:

# Gitalk
# https://github.com/gitalk/gitalk
gitalk:
  client_id:
  client_secret:
  repo:
  owner:
  admin:
  option:

# Valine
# https://valine.js.org
valine:
  appId:
  appKey:
  avatar: monsterid
  # This configuration is suitable for domestic custom domain name users, overseas version will be automatically detected (no need to manually fill in)
  serverURLs:
  bg:
  # Use Valine visitor count as the page view count
  visitor: false
  option:

# Waline - A simple comment system with backend support fork from Valine
# https://waline.js.org/
waline:
  serverURL:
  bg:
  # Use Waline pageview count as the page view count
  pageview: false
  option:

# Utterances
# https://utteranc.es/
utterances:
  repo:
  # Issue Mapping: pathname/url/title/og:title
  issue_term: pathname
  # Theme: github-light/github-dark/github-dark-orange/icy-dark/dark-blue/photon-dark
  light_theme: github-light
  dark_theme: photon-dark
  js:
  option:

# Facebook Comments Plugin
# https://developers.facebook.com/docs/plugins/comments/
facebook_comments:
  app_id:
  # optional
  user_id:
  pageSize: 10
  # Choose: social / time / reverse_time
  order_by: social
  lang: en_US

# Twikoo
# https://github.com/imaegoo/twikoo
twikoo:
  envId:
  region:
  # Use Twikoo visitor count as the page view count
  visitor: false
  option:

# Giscus
# https://giscus.app/
giscus:
  repo:
  repo_id:
  category_id:
  light_theme: light
  dark_theme: dark
  js:
  option:

# Remark42
# https://remark42.com/docs/configuration/frontend/
remark42:
  host:
  siteId:
  option:

# Artalk
# https://artalk.js.org/guide/frontend/config.html
artalk:
  server:
  site:
  # Use Artalk visitor count as the page view count
  visitor: false
  option:

# --------------------------------------
# Chat Services
# --------------------------------------

chat:
  # Choose: chatra/tidio/crisp
  # Leave it empty if you don't need chat
  use:
  # Chat Button [recommend]
  # It will create a button in the bottom right corner of website, and hide the origin button
  rightside_button: false
  # The origin chat button is displayed when scrolling up, and the button is hidden when scrolling down
  button_hide_show: false

# https://chatra.io/
chatra:
  id:

# https://www.tidio.com/
tidio:
  public_key:

# https://crisp.chat/en/
crisp:
  website_id:

# --------------------------------------
# Analysis
# --------------------------------------

# https://tongji.baidu.com/web/welcome/login
baidu_analytics:

# https://analytics.google.com/analytics/web/
google_analytics:

# https://www.cloudflare.com/zh-tw/web-analytics/
cloudflare_analytics:

# https://clarity.microsoft.com/
microsoft_clarity:

# https://umami.is/
umami_analytics:
  enable: false
  # For self-hosted setups, configure the hostname of the Umami instance
  serverURL:
  website_id:
  option:
  UV_PV:
    site_uv: false
    site_pv: false
    page_pv: false
    # Umami Cloud (API key) / self-hosted Umami (token)
    token:

# --------------------------------------
# Advertisement
# --------------------------------------

# Google Adsense
google_adsense:
  enable: false
  auto_ads: true
  js: https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js
  client:
  enable_page_level_ads: true

# Insert ads manually
# Leave it empty if you don't need ads
ad:
  # Insert ads in the index (every three posts)
  index:
  # Insert ads in aside
  aside:
  # Insert ads in the post (before pagination)
  post:

# --------------------------------------
# Verification
# --------------------------------------

site_verification:
  # - name: google-site-verification
  #   content: xxxxxx
  # - name: baidu-site-verification
  #   content: xxxxxxx

# --------------------------------------
# Beautify / Effect
# --------------------------------------

# Theme color for customize
# Notice: color value must in double quotes like "#000" or may cause error!

# theme_color:
#   enable: true
#   main: "#49B1F5"
#   paginator: "#00c4b6"
#   button_hover: "#FF7242"
#   text_selection: "#00c4b6"
#   link_color: "#99a9bf"
#   meta_color: "#858585"
#   hr_color: "#A4D8FA"
#   code_foreground: "#F47466"
#   code_background: "rgba(27, 31, 35, .05)"
#   toc_color: "#00c4b6"
#   blockquote_padding_color: "#49b1f5"
#   blockquote_background_color: "#49b1f5"
#   scrollbar_color: "#49b1f5"
#   meta_theme_color_light: "ffffff"
#   meta_theme_color_dark: "#0d0d0d"

# The user interface setting of category and tag page
# Choose: index - same as Homepage UI / default - same as archives UI
# leave it empty or index
category_ui:
tag_ui:

# Rounded corners for UI elements
rounded_corners_ui: true

# Stretches the lines so that each line has equal width
text_align_justify: false

# Add a mask to the header and footer
mask:
  header: true
  footer: true

# Loading Animation
preloader:
  enable: false
  # source
  # 1. fullpage-loading
  # 2. pace (progress bar)
  source: 1
  # pace theme (see https://codebyzach.github.io/pace/)
  pace_css_url:

# Page Transition
enter_transitions: true

# Default display mode - light (default) / dark
display_mode: light

# Configuration for beautifying the content of the article
beautify:
  enable: false
  # Specify the field to beautify (site or post)
  field: post
  # Specify the icon to be used as a prefix for the title, such as '\f0c1'
  title_prefix_icon:
  # Specify the color of the title prefix icon, such as '#F47466'
  title_prefix_icon_color:

# Global font settings
# Don't modify the following settings unless you know how they work
font:
  global_font_size:
  code_font_size:
  font_family:
  code_font_family:

# Font settings for the site title and site subtitle
blog_title_font:
  font_link:
  font_family:

# The setting of divider icon
hr_icon:
  enable: true
  # The unicode value of Font Awesome icon, such as '\3423'
  icon:
  icon_top:

# Typewriter Effect
# https://github.com/disjukr/activate-power-mode
activate_power_mode:
  enable: false
  colorful: true
  shake: true
  mobile: false

# Background effects
# --------------------------------------

# canvas_ribbon
# See: https://github.com/hustcc/ribbon.js
canvas_ribbon:
  enable: false
  # The size of ribbon
  size: 150
  # The opacity of ribbon (0 ~ 1)
  alpha: 0.6
  zIndex: -1
  click_to_change: false
  mobile: false

# Fluttering Ribbon
canvas_fluttering_ribbon:
  enable: false
  mobile: false

# canvas_nest
# https://github.com/hustcc/canvas-nest.js
canvas_nest:
  enable: false
  # Color of lines, default: '0,0,0'; RGB values: (R,G,B).(note: use ',' to separate.)
  color: '0,0,255'
  # The opacity of line (0~1)
  opacity: 0.7
  # The z-index property of the background
  zIndex: -1
  # The number of lines
  count: 99
  mobile: false

# Mouse click effects: fireworks
fireworks:
  enable: false
  zIndex: 9999
  mobile: false

# Mouse click effects: Heart symbol
click_heart:
  enable: false
  mobile: false

# Mouse click effects: words
clickShowText:
  enable: false
  text:
    # - I
    # - LOVE
    # - YOU
  fontSize: 15px
  random: false
  mobile: false

# --------------------------------------
# Lightbox Settings
# --------------------------------------

# Choose: fancybox / medium_zoom
# https://github.com/francoischalifour/medium-zoom
# https://fancyapps.com/fancybox/
# Leave it empty if you don't need lightbox
lightbox:

# --------------------------------------
# Tag Plugins settings
# --------------------------------------

# Series
series:
  enable: false
  # Order by title or date
  orderBy: 'title'
  # Sort of order. 1, asc for ascending; -1, desc for descending
  order: 1
  number: true

# ABCJS - The ABC Music Notation Plugin
# https://github.com/paulrosen/abcjs
abcjs:
  enable: false
  per_page: true

# Mermaid
# https://github.com/mermaid-js/mermaid
mermaid:
  enable: false
  # Write Mermaid diagrams using code blocks
  code_write: false
  # built-in themes: default / forest / dark / neutral
  theme:
    light: default
    dark: dark

# chartjs
# see https://www.chartjs.org/docs/latest/
chartjs:
  enable: false
  # Do not modify unless you understand how they work.
  # The default settings are only used when the MD syntax is not specified.
  # General font color for the chart
  fontColor:
    light: 'rgba(0, 0, 0, 0.8)'
    dark: 'rgba(255, 255, 255, 0.8)'
  # General border color for the chart
  borderColor:
    light: 'rgba(0, 0, 0, 0.1)'
    dark: 'rgba(255, 255, 255, 0.2)'
  # Background color for scale labels on radar and polar area charts
  scale_ticks_backdropColor:
    light: 'transparent'
    dark: 'transparent'

# Note - Bootstrap Callout
note:
  # Note tag style values:
  #  - simple    bs-callout old alert style. Default.
  #  - modern    bs-callout new (v2-v3) alert style.
  #  - flat      flat callout style with background, like on Mozilla or StackOverflow.
  #  - disabled  disable all CSS styles import of note tag.
  style: flat
  icons: true
  border_radius: 3
  # Offset lighter of background in % for modern and flat styles (modern: -12 | 12; flat: -18 | 6).
  # Offset also applied to label tag variables. This option can work with disabled note tag.
  light_bg_offset: 0

# --------------------------------------
# Other Settings
# --------------------------------------

# https://github.com/MoOx/pjax
pjax:
  enable: false
  # Exclude the specified pages from pjax, such as '/music/'
  exclude:
    # - /xxxxxx/

# Inject the css and script (aplayer/meting)
aplayerInject:
  enable: false
  per_page: true

# Snackbar - Toast Notification
# https://github.com/polonel/SnackBar
# position: top-left / top-center / top-right / bottom-left / bottom-center / bottom-right
snackbar:
  enable: false
  position: bottom-left
  # The background color of Toast Notification in light mode and dark mode
  bg_light: '#49b1f5'
  bg_dark: '#1f1f1f'

# Instant.page
# https://instant.page/
instantpage: false

# Lazyload
# https://github.com/verlok/vanilla-lazyload
lazyload:
  enable: false
  # Specify the field to use lazyload (site or post)
  field: site
  placeholder:
  blur: false

# PWA
# See https://github.com/JLHwung/hexo-offline
# ---------------
pwa:
  enable: false
  manifest:
  apple_touch_icon:
  favicon_32_32:
  favicon_16_16:
  mask_icon:

# Open graph meta tags
# https://hexo.io/docs/helpers#open-graph
Open_Graph_meta:
  enable: true
  option:
    # twitter_card:
    # twitter_image:
    # twitter_id:
    # twitter_site:
    # google_plus:
    # fb_admins:
    # fb_app_id:

# Structured Data
# https://developers.google.com/search/docs/guides/intro-structured-data
structured_data: true

# Add the vendor prefixes to ensure compatibility
css_prefix: true

# Inject
# Insert the code to head (before '</head>' tag) and the bottom (before '</body>' tag)
inject:
  head:
    # - <link rel="stylesheet" href="/xxx.css">
  bottom:
    # - <script src="xxxx"></script>

# CDN Settings
# Don't modify the following settings unless you know how they work
CDN:
  # The CDN provider for internal and third-party scripts
  # Options for both: local/jsdelivr/unpkg/cdnjs/custom
  # Note: Dev version can only use 'local' for internal scripts
  # Note: When setting third-party scripts to 'local', you need to install hexo-butterfly-extjs
  internal_provider: local
  third_party_provider: jsdelivr

  # Add version number to url, true or false
  version: false

  # Custom format
  # For example: https://cdn.staticfile.org/${cdnjs_name}/${version}/${min_cdnjs_file}
  custom_format:

  option:
    # abcjs_basic_js:
    # activate_power_mode:
    # algolia_js:
    # algolia_search:
    # aplayer_css:
    # aplayer_js:
    # artalk_css:
    # artalk_js:
    # blueimp_md5:
    # busuanzi:
    # canvas_fluttering_ribbon:
    # canvas_nest:
    # canvas_ribbon:
    # chartjs:
    # click_heart:
    # clickShowText:
    # disqusjs:
    # disqusjs_css:
    # docsearch_css:
    # docsearch_js:
    # egjs_infinitegrid:
    # fancybox:
    # fancybox_css:
    # fireworks:
    # fontawesome:
    # gitalk:
    # gitalk_css:
    # giscus:
    # instantpage:
    # instantsearch:
    # katex:
    # katex_copytex:
    # lazyload:
    # local_search:
    # main:
    # main_css:
    # mathjax:
    # medium_zoom:
    # mermaid:
    # meting_js:
    # prismjs_autoloader:
    # prismjs_js:
    # prismjs_lineNumber_js:
    # pjax:
    # sharejs:
    # sharejs_css:
    # snackbar:
    # snackbar_css:
    # translate:
    # twikoo:
    # typed:
    # utils:
    # valine:
    # waline_css:
    # waline_js:

```

### 文件路径: `themes\butterfly\package.json`
```json
{
  "name": "hexo-theme-butterfly",
  "version": "5.3.3",
  "description": "A Simple and Card UI Design theme for Hexo",
  "main": "package.json",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [
    "hexo",
    "theme",
    "butterfly",
    "Card UI Design",
    "Jerry",
    "hexo-theme-butterfly"
  ],
  "repository": {
    "type" : "git",
    "url" : "https://github.com/jerryc127/hexo-theme-butterfly.git"
  },
  "bugs": {
    "url": "https://github.com/jerryc127/hexo-theme-butterfly/issues",
    "email": "my@crazywong.com"
  },
  "dependencies": {
    "hexo-renderer-stylus": "^3.0.1",
    "hexo-renderer-pug": "^3.0.0"
  },
  "homepage": "https://butterfly.js.org/",
  "author": "Jerry <my@crazywong.com>",
  "license": "Apache-2.0"
}

```

### 文件路径: `themes\butterfly\plugins.yml`
```yml
abcjs_basic_js:
  name: abcjs
  file: dist/abcjs-basic-min.js
  version: 6.4.4
activate_power_mode:
  name: butterfly-extsrc
  file: dist/activate-power-mode.min.js
  version: 1.1.4
algolia_search:
  name: algoliasearch
  file: dist/lite/builds/browser.umd.js
  version: 5.20.2
aplayer_css:
  name: aplayer
  file: dist/APlayer.min.css
  version: 1.10.1
aplayer_js:
  name: aplayer
  file: dist/APlayer.min.js
  version: 1.10.1
artalk_css:
  name: artalk
  file: dist/Artalk.css
  version: 2.9.1
artalk_js:
  name: artalk
  file: dist/Artalk.js
  version: 2.9.1
blueimp_md5:
  name: blueimp-md5
  file: js/md5.min.js
  version: 2.19.0
canvas_fluttering_ribbon:
  name: butterfly-extsrc
  file: dist/canvas-fluttering-ribbon.min.js
  version: 1.1.4
canvas_nest:
  name: butterfly-extsrc
  file: dist/canvas-nest.min.js
  version: 1.1.4
canvas_ribbon:
  name: butterfly-extsrc
  file: dist/canvas-ribbon.min.js
  version: 1.1.4
chartjs:
  name: chart.js
  file: dist/chart.umd.js
  version: 4.4.7
clickShowText:
  name: butterfly-extsrc
  file: dist/click-show-text.min.js
  version: 1.1.4
click_heart:
  name: butterfly-extsrc
  file: dist/click-heart.min.js
  version: 1.1.4
disqusjs:
  name: disqusjs
  file: dist/browser/disqusjs.es2015.umd.min.js
  version: 3.0.2
disqusjs_css:
  name: disqusjs
  file: dist/browser/styles/disqusjs.css
  version: 3.0.2
docsearch_css:
  name: '@docsearch/css'
  other_name: docsearch-css
  file: dist/style.css
  version: 3.8.3
docsearch_js:
  name: '@docsearch/js'
  other_name: docsearch-js
  file: dist/umd/index.js
  version: 3.8.3
egjs_infinitegrid:
  name: '@egjs/infinitegrid'
  other_name: egjs-infinitegrid
  file: dist/infinitegrid.min.js
  version: 4.12.0
fancybox:
  name: '@fancyapps/ui'
  file: dist/fancybox/fancybox.umd.js
  version: 5.0.36
  other_name: fancyapps-ui
fancybox_css:
  name: '@fancyapps/ui'
  file: dist/fancybox/fancybox.css
  version: 5.0.36
  other_name: fancyapps-ui
fireworks:
  name: butterfly-extsrc
  file: dist/fireworks.min.js
  version: 1.1.4
fontawesome:
  name: '@fortawesome/fontawesome-free'
  file: css/all.min.css
  other_name: font-awesome
  version: 6.7.2
gitalk:
  name: gitalk
  file: dist/gitalk.min.js
  version: 1.8.0
gitalk_css:
  name: gitalk
  file: dist/gitalk.css
  version: 1.8.0
instantpage:
  name: instant.page
  file: instantpage.js
  version: 5.2.0
instantsearch:
  name: instantsearch.js
  file: dist/instantsearch.production.min.js
  version: 4.77.3
katex:
  name: katex
  file: dist/katex.min.css
  other_name: KaTeX
  version: 0.16.21
katex_copytex:
  name: katex
  file: dist/contrib/copy-tex.min.js
  other_name: KaTeX
  version: 0.16.21
lazyload:
  name: vanilla-lazyload
  file: dist/lazyload.iife.min.js
  version: 19.1.3
mathjax:
  name: mathjax
  file: es5/tex-mml-chtml.js
  version: 3.2.2
medium_zoom:
  name: medium-zoom
  file: dist/medium-zoom.min.js
  version: 1.1.0
mermaid:
  name: mermaid
  file: dist/mermaid.min.js
  version: 11.4.1
meting_js:
  name: butterfly-extsrc
  file: metingjs/dist/Meting.min.js
  version: 1.1.4
pace_default_css:
  name: pace-js
  other_name: pace
  file: themes/blue/pace-theme-minimal.css
  version: 1.2.4
pace_js:
  name: pace-js
  other_name: pace
  file: pace.min.js
  version: 1.2.4
pjax:
  name: pjax
  file: pjax.min.js
  version: 0.2.8
prismjs_autoloader:
  name: prismjs
  file: plugins/autoloader/prism-autoloader.min.js
  other_name: prism
  version: 1.29.0
prismjs_js:
  name: prismjs
  file: prism.js
  other_name: prism
  version: 1.29.0
prismjs_lineNumber_js:
  name: prismjs
  file: plugins/line-numbers/prism-line-numbers.min.js
  other_name: prism
  version: 1.29.0
sharejs:
  name: butterfly-extsrc
  file: sharejs/dist/js/social-share.min.js
  version: 1.1.4
sharejs_css:
  name: butterfly-extsrc
  file: sharejs/dist/css/share.min.css
  version: 1.1.4
snackbar:
  name: node-snackbar
  file: dist/snackbar.min.js
  version: 0.1.16
snackbar_css:
  name: node-snackbar
  file: dist/snackbar.min.css
  version: 0.1.16
twikoo:
  name: twikoo
  file: dist/twikoo.all.min.js
  version: 1.6.41
typed:
  name: typed.js
  file: dist/typed.umd.js
  version: 2.1.0
valine:
  name: valine
  file: dist/Valine.min.js
  version: 1.5.3
waline_css:
  name: '@waline/client'
  file: dist/waline.css
  other_name: waline
  version: 3.5.2
waline_js:
  name: '@waline/client'
  file: dist/waline.js
  other_name: waline
  version: 3.5.2

```

### 文件路径: `themes\butterfly\.github\FUNDING.yml`
```yml
# These are supported funding model platforms

github: # Replace with up to 4 GitHub Sponsors-enabled usernames e.g., [user1, user2]
patreon: # Replace with a single Patreon username
open_collective: # Replace with a single Open Collective username
ko_fi: # Replace with a single Ko-fi username
tidelift: # Replace with a single Tidelift platform-name/package-name e.g., npm/babel
community_bridge: # Replace with a single Community Bridge project-name e.g., cloud-foundry
liberapay: # Replace with a single Liberapay username
issuehunt: # Replace with a single IssueHunt username
otechie: # Replace with a single Otechie username
lfx_crowdfunding: # Replace with a single LFX Crowdfunding project-name e.g., cloud-foundry
custom: ['https://buy.stripe.com/3cs6rP6YA91sbbG5kk','https://jsd.012700.xyz/gh/jerryc127/CDN/Photo/wechat.jpg'] # Replace with up to 4 custom sponsorship URLs e.g., ['link1', 'link2']

```

### 文件路径: `themes\butterfly\.github\ISSUE_TEMPLATE\bug_report.yml`
```yml
name: Bug report
description: Create a report to help us improve
title: '[Bug]: '

body:
  - type: markdown
    attributes:
      value: |
        重要：請依照該模板來提交 
        Important: Please follow the template to create a new issue

  - type: input
    id: butterfly-ver
    attributes:
      label: 使用的 Butterfly 版本？ | What version of Butterfly are you using?
      description: 檢視主題的 package.json | Check the theme's package.json
    validations:
      required: true

  - type: dropdown
    id: modify
    attributes:
      label: 是否修改過主題文件？ | Has the theme files been modified?
      options:
        - 是 (Yes)
        - 否 (No)
    validations:
      required: true

  - type: dropdown
    id: browser
    attributes:
      label: 使用的瀏覽器？ | What browser are you using?
      options:
        - Chrome
        - Edge
        - Safari
        - Opera
        - Other
    validations:
      required: true

  - type: dropdown
    id: platform
    attributes:
      label: 使用的系統？ | What operating system are you using?
      options:
        - Windows
        - macOS 
        - Linux
        - Android
        - iOS
        - Other
    validations:
      required: true

  - type: textarea
    id: dependencies
    attributes:
      label: 依賴插件 | Package dependencies information
      description: 在 Hexo 根目錄下執行 `npm ls --depth 0` | Run `npm ls --depth 0` in Hexo root directory
      render: Text
    validations:
      required: true

  - type: textarea
    id: description
    attributes:
      label: 問題描述 | Describe the bug
      description: 請描述你的問題現象 | A clear and concise description of what the bug is.
      placeholder: 請儘量提供截圖來定位問題 | If applicable, add screenshots to help explain your problem
      value:
    validations:
      required: true

  - type: input
    id: website
    attributes:
      label: 出現問題的網站 | Website with the issue
      description: 請提供可復現問題的網站地址 | Please provide a website URL where the problem can be reproduced.
      placeholder: 請填寫具體的網址，不要填寫 localhost 網站 | Please provide a specific URL, do not use localhost. 
    validations:
      required: true
```

### 文件路径: `themes\butterfly\.github\ISSUE_TEMPLATE\config.yml`
```yml
blank_issues_enabled: false
contact_links:
  - name: Questions about Butterfly
    url: https://github.com/jerryc127/hexo-theme-butterfly/discussions
    about: 一些使用問題請到 Discussion 詢問。 Please ask questions in Discussion.

  - name: Butterfly Q&A
    url: https://butterfly.js.org/posts/98d20436/
    about: Butterfly Q&A

  - name: Telegram
    url: https://t.me/bu2fly
    about: 'Official Telegram Group'

  - name: QQ 群
    url: https://jq.qq.com/?_wv=1027&k=KU9105XR
    about: '群號 1070540070'


```

### 文件路径: `themes\butterfly\.github\ISSUE_TEMPLATE\feature_request.yml`
```yml
name: Feature request
description: Suggest an idea for this project
title: '[Feature]: '

body:
  - type: textarea
    id: feature-request
    attributes:
      label: 想要的功能 | What feature do you want?
      description: 請描述你需要的新功能 | A clear and concise description of what the feature is.
      placeholder:
      value:
    validations:
      require: true
```

### 文件路径: `themes\butterfly\.github\workflows\publish.yml`
```yml
name: npm publish

on:
  release:
    types: [created]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    # Setup .npmrc file to publish to npm
    - uses: actions/setup-node@v1
      with:
        node-version: '12.x'
        registry-url: 'https://registry.npmjs.org'
    - run: npm install
    - run: npm publish
      env:
        NODE_AUTH_TOKEN: ${{ secrets.NPM_TOKEN }}
```

### 文件路径: `themes\butterfly\.github\workflows\stale.yml`
```yml
name: 'Close stale issues and PRs'
on:
  schedule:
    - cron: '30 1 * * *'

jobs:
  stale:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/stale@v5
        with:
          days-before-issue-stale: 30
          days-before-pr-stale: -1
          days-before-close: 7
          stale-issue-message: 'This issue has been automatically marked as stale because it has not had recent activity. It will be closed if no further activity occurs. Thank you for your contributions.'
          close-pr-message: 'This issue has not seen any activity since it was marked stale. Closing.'
          stale-issue-label: 'Stale'
          exempt-issue-labels: 'pinned,bug,enhancement,documentation,Plan'
          operations-per-run: 1000
```

### 文件路径: `themes\butterfly\languages\default.yml`
```yml
footer:
  framework: Framework
  theme: Theme

copy:
  success: Copy Successful
  error: Copy Failed
  noSupport: Browser Not Supported

page:
  articles: All Articles
  tag: Tag
  category: Category
  archives: Archives

card_post_count: comments

no_title: Untitled

post:
  created: Created
  updated: Updated
  wordcount: Word Count
  min2read: Reading Time
  min2read_unit: mins
  page_pv: Post Views
  comments: Comments
  copyright:
    author: Author
    link: Link
    copyright_notice: Copyright Notice
    copyright_content: 'All articles on this blog are licensed under <a href="%s">%s</a> unless otherwise stated.'
  recommend: Related Articles
  edit: Edit

search:
  title: Search
  load_data: Loading Database
  input_placeholder: Search for Posts
  algolia_search:
    hits_empty: 'No results found for: ${query}'
    hits_stats: '${hits} results found in ${time} ms'
  local_search:
    hits_empty: 'No results found for: ${query}'
    hits_stats: '${hits} articles found'

pagination:
  prev: Previous
  next: Next

comment: Comments

aside:
  articles: Articles
  tags: Tags
  categories: Categories
  card_announcement: Announcement
  card_categories: Categories
  card_tags: Tags
  card_archives: Archives
  card_recent_post: Recent Posts
  card_webinfo:
    headline: Website Info
    article_name: Article Count
    runtime:
      name: Runtime
      unit: days
    last_push_date:
      name: Last Update
    site_wordcount: Total Word Count
    site_uv_name: Unique Visitors
    site_pv_name: Page Views
  more_button: View More
  card_newest_comments:
    headline: Latest Comments
    loading_text: Loading...
    error: Unable to retrieve comments, please check the configuration
    zero: No comments
    image: Image
    link: Link
    code: Code
  card_toc: Contents
  card_post_series: Post Series

date_suffix:
  just: Just now
  min: minutes ago
  hour: hours ago
  day: days ago
  month: months ago

donate: Sponsor
share: Share

rightside:
  readmode_title: Reading Mode
  translate_title: Toggle Between Traditional and Simplified Chinese
  night_mode_title: Toggle Between Light and Dark Mode
  back_to_top: Back to Top
  toc: Table of Contents
  scroll_to_comment: Scroll to Comments
  setting: Settings
  aside: Toggle Between Single-column and Double-column
  chat: Chat

copy_copyright:
  author: Author
  link: Link
  source: Source
  info: Copyright belongs to the author. For commercial use, please contact the author for authorization. For non-commercial use, please indicate the source.

Snackbar:
  chs_to_cht: You have switched to Traditional Chinese
  cht_to_chs: You have switched to Simplified Chinese
  day_to_night: You have switched to Dark Mode
  night_to_day: You have switched to Light Mode

loading: Loading...
load_more: Load More

error404: Page Not Found

```

### 文件路径: `themes\butterfly\languages\en.yml`
```yml
footer:
  framework: Framework
  theme: Theme

copy:
  success: Copy Successful
  error: Copy Failed
  noSupport: Browser Not Supported

page:
  articles: All Articles
  tag: Tag
  category: Category
  archives: Archives

card_post_count: comments

no_title: Untitled

post:
  created: Created
  updated: Updated
  wordcount: Word Count
  min2read: Reading Time
  min2read_unit: mins
  page_pv: Post Views
  comments: Comments
  copyright:
    author: Author
    link: Link
    copyright_notice: Copyright Notice
    copyright_content: 'All articles on this blog are licensed under <a href="%s">%s</a> unless otherwise stated.'
  recommend: Related Articles
  edit: Edit

search:
  title: Search
  load_data: Loading Database
  input_placeholder: Search for Posts
  algolia_search:
    hits_empty: 'No results found for: ${query}'
    hits_stats: '${hits} results found in ${time} ms'
  local_search:
    hits_empty: 'No results found for: ${query}'
    hits_stats: '${hits} articles found'

pagination:
  prev: Previous
  next: Next

comment: Comments

aside:
  articles: Articles
  tags: Tags
  categories: Categories
  card_announcement: Announcement
  card_categories: Categories
  card_tags: Tags
  card_archives: Archives
  card_recent_post: Recent Posts
  card_webinfo:
    headline: Website Info
    article_name: Article Count
    runtime:
      name: Runtime
      unit: days
    last_push_date:
      name: Last Update
    site_wordcount: Total Word Count
    site_uv_name: Unique Visitors
    site_pv_name: Page Views
  more_button: View More
  card_newest_comments:
    headline: Latest Comments
    loading_text: Loading...
    error: Unable to retrieve comments, please check the configuration
    zero: No comments
    image: Image
    link: Link
    code: Code
  card_toc: Contents
  card_post_series: Post Series

date_suffix:
  just: Just now
  min: minutes ago
  hour: hours ago
  day: days ago
  month: months ago

donate: Sponsor
share: Share

rightside:
  readmode_title: Reading Mode
  translate_title: Toggle Between Traditional and Simplified Chinese
  night_mode_title: Toggle Between Light and Dark Mode
  back_to_top: Back to Top
  toc: Table of Contents
  scroll_to_comment: Scroll to Comments
  setting: Settings
  aside: Toggle Between Single-column and Double-column
  chat: Chat

copy_copyright:
  author: Author
  link: Link
  source: Source
  info: Copyright belongs to the author. For commercial use, please contact the author for authorization. For non-commercial use, please indicate the source.

Snackbar:
  chs_to_cht: You have switched to Traditional Chinese
  cht_to_chs: You have switched to Simplified Chinese
  day_to_night: You have switched to Dark Mode
  night_to_day: You have switched to Light Mode

loading: Loading...
load_more: Load More

error404: Page Not Found

```

### 文件路径: `themes\butterfly\languages\ja.yml`
```yml
footer:
  framework: フレームワーク
  theme: テーマ

copy:
  success: コピー成功
  error: コピー失敗
  noSupport: ブラウザが対応していません

page:
  articles: 記事一覧
  tag: タグ
  category: カテゴリ
  archives: アーカイブ

card_post_count: コメント数

no_title: タイトルなし

post:
  created: 作成日
  updated: 更新日
  wordcount: 総文字数
  min2read: 読む時間
  min2read_unit: 分
  page_pv: 閲覧数
  comments: コメント数
  copyright:
    author: 著者
    link: リンク
    copyright_notice: 著作権表示
    copyright_content: 'このブログのすべての記事は、<a href="%s">%s</a> ライセンスの下で提供されており、特に明記されていない限り、すべての権利を留保します。転載時には出典を明記してください: <a href="%s">%s</a>。'
  recommend: 関連記事
  edit: 編集

search:
  title: 検索
  load_data: データベースを読み込んでいます
  input_placeholder: 記事を検索
  algolia_search:
    hits_empty: '${query} の検索結果が見つかりませんでした。'
    hits_stats: '${hits} 件の結果が ${time}ms で見つかりました'
  local_search:
    hits_empty: '${query} の検索結果が見つかりませんでした。'
    hits_stats: '${hits} 件の記事が見つかりました'

pagination:
  prev: 前へ
  next: 次へ

comment: コメント

aside:
  articles: 記事
  tags: タグ
  categories: カテゴリ
  card_announcement: お知らせ
  card_categories: カテゴリ
  card_tags: タグ
  card_archives: アーカイブ
  card_recent_post: 最近の記事
  card_webinfo:
    headline: サイト情報
    article_name: 記事数
    runtime:
      name: 稼働時間
      unit: 日
    last_push_date:
      name: 最終更新日
    site_wordcount: 総文字数
    site_uv_name: ユーザー数
    site_pv_name: ページビュー数
  more_button: もっと見る
  card_newest_comments:
    headline: 最新コメント
    loading_text: ローディング中...
    error: コメントを取得できませんでした。設定を確認してください。
    zero: コメントがありません
    image: 画像
    link: リンク
    code: コード
  card_toc: 目次
  card_post_series: シリーズ記事

date_suffix:
  just: たった今
  min: 分前
  hour: 時間前
  day: 日前
  month: ヶ月前

donate: 寄付
share: 共有

rightside:
  readmode_title: 読書モード
  translate_title: 簡体字と繁体字の切り替え
  night_mode_title: ライトモード/ダークモード切り替え
  back_to_top: トップに戻る
  toc: 目次
  scroll_to_comment: コメントへ移動
  setting: 設定
  aside: シングルカラムとダブルカラムの切り替え
  chat: チャット

copy_copyright:
  author: 著者
  link: リンク
  source: ソース
  info: 著作権は著者に帰属します。商業的利用の場合は著者に連絡して許可を得てください。非商業的利用の場合は出典を明記してください。

Snackbar:
  chs_to_cht: 繁体字に切り替えました
  cht_to_chs: 簡体字に切り替えました
  day_to_night: ダークモードに切り替えました
  night_to_day: ライトモードに切り替えました

loading: ローディング中...
load_more: もっと見る

error404: ページが見つかりません

```

### 文件路径: `themes\butterfly\languages\ko.yml`
```yml
footer:
  framework: 프레임워크
  theme: 테마

copy:
  success: 복사 성공
  error: 복사 실패
  noSupport: 브라우저가 지원되지 않음

page:
  articles: 모든 글
  tag: 태그
  category: 카테고리
  archives: 아카이브

card_post_count: 댓글 수

no_title: 제목 없음

post:
  created: 작성일
  updated: 수정일
  wordcount: 총 글자 수
  min2read: 읽기 시간
  min2read_unit: 분
  page_pv: 조회수
  comments: 댓글
  copyright:
    author: 작성자
    link: 링크
    copyright_notice: 저작권 고지
    copyright_content: '이 블로그의 모든 글은 <a href="%s">%s</a> 라이선스를 따르며, 별도로 명시되지 않는 한 모든 권리를 보유합니다. 재배포 시 출처를 명시해 주세요: <a href="%s">%s</a>.'
  recommend: 관련 글
  edit: 편집

search:
  title: 검색
  load_data: 데이터베이스 로드 중
  input_placeholder: 글 검색
  algolia_search:
    hits_empty: '${query}에 대한 결과를 찾을 수 없습니다.'
    hits_stats: '${hits}개의 결과를 ${time}ms 만에 찾음'
  local_search:
    hits_empty: '${query}에 대한 결과를 찾을 수 없습니다.'
    hits_stats: '${hits}개의 글을 찾음'

pagination:
  prev: 이전
  next: 다음

comment: 댓글

aside:
  articles: 글
  tags: 태그
  categories: 카테고리
  card_announcement: 공지
  card_categories: 카테고리
  card_tags: 태그
  card_archives: 아카이브
  card_recent_post: 최근 글
  card_webinfo:
    headline: 사이트 정보
    article_name: 글 수
    runtime:
      name: 운영 시간
      unit: 일
    last_push_date:
      name: 마지막 업데이트
    site_wordcount: 총 글자 수
    site_uv_name: 방문자 수
    site_pv_name: 총 조회수
  more_button: 더 보기
  card_newest_comments:
    headline: 최신 댓글
    loading_text: 로딩 중...
    error: 댓글을 가져올 수 없습니다. 설정을 확인해 주세요.
    zero: 댓글 없음
    image: 이미지
    link: 링크
    code: 코드
  card_toc: 목차
  card_post_series: 시리즈 글

date_suffix:
  just: 방금
  min: 분 전
  hour: 시간 전
  day: 일 전
  month: 달 전

donate: 후원
share: 공유

rightside:
  readmode_title: 읽기 모드
  translate_title: 번체와 간체 전환
  night_mode_title: 라이트/다크 모드 전환
  back_to_top: 맨 위로
  toc: 목차
  scroll_to_comment: 댓글로 이동
  setting: 설정
  aside: 단일/이중 열 전환
  chat: 채팅

copy_copyright:
  author: 작성자
  link: 링크
  source: 출처
  info: 저작권은 작성자에게 있습니다. 상업적 사용을 위해서는 작성자의 허가를 받아야 하며, 비상업적 사용 시에는 출처를 명시해 주세요.

Snackbar:
  chs_to_cht: 번체로 전환되었습니다.
  cht_to_chs: 간체로 전환되었습니다.
  day_to_night: 다크 모드로 전환되었습니다.
  night_to_day: 라이트 모드로 전환되었습니다.

loading: 로딩 중...
load_more: 더 보기

error404: 페이지를 찾을 수 없습니다.

```

### 文件路径: `themes\butterfly\languages\zh-CN.yml`
```yml
footer:
  framework: 框架
  theme: 主题

copy:
  success: 复制成功
  error: 复制失败
  noSupport: 浏览器不支持

page:
  articles: 全部文章
  tag: 标签
  category: 分类
  archives: 归档

card_post_count: 条评论

no_title: 无标题

post:
  created: 发表于
  updated: 更新于
  wordcount: 总字数
  min2read: 阅读时长
  min2read_unit: 分钟
  page_pv: 浏览量
  comments: 评论数
  copyright:
    author: 文章作者
    link: 文章链接
    copyright_notice: 版权声明
    copyright_content: '本博客所有文章除特别声明外，均采用
      <a href="%s" target="_blank">%s</a> 许可协议。转载请注明来源 <a href="%s" target="_blank">%s</a>！'
  recommend: 相关推荐
  edit: 编辑

search:
  title: 搜索
  load_data: 数据加载中
  input_placeholder: 搜索文章
  algolia_search:
    hits_empty: '未找到符合您查询的内容：${query}'
    hits_stats: '找到 ${hits} 条结果，耗时 ${time} 毫秒'
  local_search:
    hits_empty: '未找到符合您查询的内容：${query}'
    hits_stats: '共找到 ${hits} 篇文章'

pagination:
  prev: 上一篇
  next: 下一篇

comment: 评论

aside:
  articles: 文章
  tags: 标签
  categories: 分类
  card_announcement: 公告
  card_categories: 分类
  card_tags: 标签
  card_archives: 归档
  card_recent_post: 最新文章
  card_webinfo:
    headline: 网站信息
    article_name: 文章数目
    runtime:
      name: 运行时间
      unit: 天
    last_push_date:
      name: 最后更新时间
    site_wordcount: 本站总字数
    site_uv_name: 本站访客数
    site_pv_name: 本站总浏览量
  more_button: 查看更多
  card_newest_comments:
    headline: 最新评论
    loading_text: 加载中...
    error: 无法获取评论，请确认相关配置是否正确
    zero: 暂无评论
    image: 图片
    link: 链接
    code: 代码
  card_toc: 目录
  card_post_series: 系列文章

date_suffix:
  just: 刚刚
  min: 分钟前
  hour: 小时前
  day: 天前
  month: 个月前

donate: 赞助
share: 分享

rightside:
  readmode_title: 阅读模式
  translate_title: 简繁转换
  night_mode_title: 日间和夜间模式切换
  back_to_top: 回到顶部
  toc: 目录
  scroll_to_comment: 前往评论
  setting: 设置
  aside: 单栏和双栏切换
  chat: 聊天

copy_copyright:
  author: 作者
  link: 链接
  source: 来源
  info: 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

Snackbar:
  chs_to_cht: 已切换为繁体中文
  cht_to_chs: 已切换为简体中文
  day_to_night: 已切换为深色模式
  night_to_day: 已切换为浅色模式

loading: 加载中...
load_more: 加载更多

error404: 页面未找到

```

### 文件路径: `themes\butterfly\languages\zh-HK.yml`
```yml
footer:
  framework: 框架
  theme: 主題

copy:
  success: 複製成功
  error: 複製失敗
  noSupport: 瀏覽器不支援

page:
  articles: 全部文章
  tag: 標籤
  category: 分類
  archives: 歸檔

card_post_count: 條評論

no_title: 無標題

post:
  created: 發表於
  updated: 更新於
  wordcount: 字數統計
  min2read: 閱讀時間
  min2read_unit: 分鐘
  page_pv: 瀏覽量
  comments: 評論數
  copyright:
    author: 文章作者
    link: 文章連結
    copyright_notice: 版權聲明
    copyright_content: '除特別聲明外，本博客所有文章均採用<a href="%s">%s</a> 授權協議。轉載請註明出處：<a href="%s">%s</a>。'
  recommend: 相關文章
  edit: 編輯

search:
  title: 搜尋
  load_data: 正在加載數據庫
  input_placeholder: 搜尋文章
  algolia_search:
    hits_empty: '未找到相關內容：${query}'
    hits_stats: '找到 ${hits} 條結果，耗時 ${time} 毫秒'
  local_search:
    hits_empty: '未找到相關內容：${query}'
    hits_stats: '找到 ${hits} 篇文章'

pagination:
  prev: 上一頁
  next: 下一頁

comment: 評論

aside:
  articles: 文章
  tags: 標籤
  categories: 分類
  card_announcement: 公告
  card_categories: 分類
  card_tags: 標籤
  card_archives: 歸檔
  card_recent_post: 最新文章
  card_webinfo:
    headline: 網站資訊
    article_name: 文章數目
    runtime:
      name: 運行時間
      unit: 天
    last_push_date:
      name: 最後更新時間
    site_wordcount: 總字數
    site_uv_name: 訪客數
    site_pv_name: 總瀏覽量
  more_button: 查看更多
  card_newest_comments:
    headline: 最新評論
    loading_text: 正在加載...
    error: 無法取得評論，請確認配置是否正確
    zero: 暫無評論
    image: 圖片
    link: 連結
    code: 代碼
  card_toc: 目錄
  card_post_series: 系列文章

date_suffix:
  just: 剛剛
  min: 分鐘前
  hour: 小時前
  day: 天前
  month: 個月前

donate: 贊助
share: 分享

rightside:
  readmode_title: 閱讀模式
  translate_title: 簡繁轉換
  night_mode_title: 切換日夜模式
  back_to_top: 回到頂部
  toc: 目錄
  scroll_to_comment: 前往評論
  setting: 設定
  aside: 單欄與雙欄切換
  chat: 聊天

copy_copyright:
  author: 作者
  link: 連結
  source: 來源
  info: 版權屬於作者所有。商業用途請聯絡作者獲得授權，非商業用途請註明出處。

Snackbar:
  chs_to_cht: 已切換為繁體中文
  cht_to_chs: 已切換為簡體中文
  day_to_night: 已切換為深色模式
  night_to_day: 已切換為淺色模式

loading: 正在加載...
load_more: 加載更多

error404: 未找到頁面

```

### 文件路径: `themes\butterfly\languages\zh-TW.yml`
```yml
footer:
  framework: 框架
  theme: 主題

copy:
  success: 複製成功
  error: 複製失敗
  noSupport: 瀏覽器不支援

page:
  articles: 所有文章
  tag: 標籤
  category: 分類
  archives: 歸檔

card_post_count: 則評論

no_title: 無標題

post:
  created: 發表於
  updated: 更新於
  wordcount: 總字數
  min2read: 閱讀時間
  min2read_unit: 分鐘
  page_pv: 瀏覽量
  comments: 評論數
  copyright:
    author: 文章作者
    link: 文章連結
    copyright_notice: 版權聲明
    copyright_content: '本部落格所有文章除特別聲明外，均採用<a href="%s" target="_blank">%s</a> 授權協議。轉載請註明來源 <a href="%s" target="_blank">%s</a>！'
  recommend: 相關推薦
  edit: 編輯

search:
  title: 搜尋
  load_data: 資料載入中
  input_placeholder: 搜尋文章
  algolia_search:
    hits_empty: '找不到符合您查詢的內容：${query}'
    hits_stats: '找到 ${hits} 筆結果，耗時 ${time} 毫秒'
  local_search:
    hits_empty: '找不到符合您查詢的內容：${query}'
    hits_stats: '共找到 ${hits} 篇文章'

pagination:
  prev: 上一篇
  next: 下一篇

comment: 評論

aside:
  articles: 文章
  tags: 標籤
  categories: 分類
  card_announcement: 公告
  card_categories: 分類
  card_tags: 標籤
  card_archives: 歸檔
  card_recent_post: 最新文章
  card_webinfo:
    headline: 網站資訊
    article_name: 文章數量
    runtime:
      name: 運行時間
      unit: 天
    last_push_date:
      name: 最後更新時間
    site_wordcount: 總字數
    site_uv_name: 訪客數
    site_pv_name: 總瀏覽量
  more_button: 檢視更多
  card_newest_comments:
    headline: 最新評論
    loading_text: 載入中...
    error: 無法獲取評論，請確認相關配置是否正確
    zero: 尚無評論
    image: 圖片
    link: 連結
    code: 程式碼
  card_toc: 目錄
  card_post_series: 系列文章

date_suffix:
  just: 剛剛
  min: 分鐘前
  hour: 小時前
  day: 天前
  month: 個月前

donate: 贊助
share: 分享

rightside:
  readmode_title: 閱讀模式
  translate_title: 繁簡轉換
  night_mode_title: 日夜模式切換
  back_to_top: 回到頂端
  toc: 目錄
  scroll_to_comment: 前往評論
  setting: 設定
  aside: 單欄和雙欄切換
  chat: 聊天

copy_copyright:
  author: 作者
  link: 連結
  source: 來源
  info: 著作權歸作者所有。如需商業轉載，請聯絡作者獲得授權，非商業轉載請註明出處。

Snackbar:
  chs_to_cht: 已切換為繁體中文
  cht_to_chs: 已切換為簡體中文
  day_to_night: 已切換為深色模式
  night_to_day: 已切換為淺色模式

loading: 載入中...
load_more: 載入更多

error404: 找不到頁面

```

### 文件路径: `themes\butterfly\layout\archive.pug`
```pug
extends includes/layout.pug

block content
  include ./includes/mixins/article-sort.pug
  #archive
    .article-sort-title= `${_p('page.articles')} - ${getArchiveLength()}`
    +articleSort(page.posts)
    include includes/pagination.pug
```

### 文件路径: `themes\butterfly\layout\category.pug`
```pug
extends includes/layout.pug

block content
  if theme.category_ui == 'index'
    include ./includes/mixins/indexPostUI.pug
    +indexPostUI
  else
    include ./includes/mixins/article-sort.pug
    #category
      .article-sort-title= _p('page.category') + ' - ' + page.category
      +articleSort(page.posts)
      include includes/pagination.pug
```

### 文件路径: `themes\butterfly\layout\index.pug`
```pug
extends includes/layout.pug

block content
  include ./includes/mixins/indexPostUI.pug
  +indexPostUI
```

### 文件路径: `themes\butterfly\layout\page.pug`
```pug
extends includes/layout.pug

block content
  - const noCardLayout = ['shuoshuo', '404'].includes(page.type) ? 'nc' : ''
  - var commentsJsLoad = false

  mixin commentLoad
    if page.comments !== false && theme.comments.use
      - commentsJsLoad = true
      !=partial('includes/third-party/comments/index', {}, {cache: true})

  #page(class=noCardLayout)
    if top_img === false && page.title
      .page-title= page.title

    case page.type
      when 'tags'
        include includes/page/tags.pug
        +commentLoad
      when 'link'
        include includes/page/flink.pug
        +commentLoad
      when 'categories'
        include includes/page/categories.pug
        +commentLoad
      when '404'
        include includes/page/404.pug
      when 'shuoshuo'
        include includes/page/shuoshuo.pug
      default
        include includes/page/default-page.pug
        +commentLoad
```

### 文件路径: `themes\butterfly\layout\post.pug`
```pug
extends includes/layout.pug

block content
  #post
    if top_img === false
      include includes/header/post-info.pug

    article#article-container.container.post-content
      if theme.noticeOutdate.enable && page.noticeOutdate !== false
        include includes/post/outdate-notice.pug
      else
        !=page.content
    include includes/post/post-copyright.pug
    .tag_share
      if (page.tags.length > 0 && theme.post_meta.post.tags)
        .post-meta__tag-list
          each item, index in page.tags.data
            a(href=url_for(item.path)).post-meta__tags #[=item.name]
      include includes/third-party/share/index.pug

    if theme.reward.enable && theme.reward.QR_code
      !=partial('includes/post/reward', {}, {cache: true})

    //- ad
    if theme.ad && theme.ad.post
      .ads-wrap!=theme.ad.post

    if theme.post_pagination
      include includes/pagination.pug
    if theme.related_post && theme.related_post.enable
      != related_posts(page,site.posts)

    if page.comments !== false && theme.comments.use
      - var commentsJsLoad = true
      !=partial('includes/third-party/comments/index', {}, {cache: true})

```

### 文件路径: `themes\butterfly\layout\tag.pug`
```pug
extends includes/layout.pug

block content
  if theme.tag_ui == 'index'
    include ./includes/mixins/indexPostUI.pug
    +indexPostUI
  else
    include ./includes/mixins/article-sort.pug
    #tag
      .article-sort-title= _p('page.tag') + ' - ' + page.tag
      +articleSort(page.posts)
      include includes/pagination.pug
```

### 文件路径: `themes\butterfly\layout\includes\additional-js.pug`
```pug
div
  script(src=url_for(theme.asset.utils))
  script(src=url_for(theme.asset.main))

  if theme.translate.enable
    script(src=url_for(theme.asset.translate))

  if theme.lightbox
    script(src=url_for(theme.asset[theme.lightbox]))

  if theme.instantpage
    script(src=url_for(theme.asset.instantpage), type='module')

  if theme.lazyload.enable && !theme.lazyload.native
    script(src=url_for(theme.asset.lazyload))

  if theme.snackbar.enable
    script(src=url_for(theme.asset.snackbar))

  .js-pjax
    if needLoadCountJs
      != partial("includes/third-party/card-post-count/index", {}, { cache: true })

    if loadSubJs
      include ./third-party/subtitle.pug

    include ./third-party/math/index.pug
    include ./third-party/abcjs/index.pug

    if commentsJsLoad
      include ./third-party/comments/js.pug

  != partial("includes/third-party/prismjs", {}, { cache: true })

  if theme.aside.enable && theme.aside.card_newest_comments.enable
    if theme.pjax.enable || (globalPageType !== 'post' && page.aside !== false)
      != partial("includes/third-party/newest-comments/index", {}, { cache: true })

  != fragment_cache('injectBottom', function(){return injectHtml(theme.inject.bottom)})

  != partial("includes/third-party/effect", {}, { cache: true })
  != partial("includes/third-party/chat/index", {}, { cache: true })

  if theme.aplayerInject && theme.aplayerInject.enable
    if theme.pjax.enable || theme.aplayerInject.per_page || page.aplayer
      include ./third-party/aplayer.pug

  if theme.pjax.enable
    != partial("includes/third-party/pjax", {}, { cache: true })

  if theme.umami_analytics.enable
    != partial("includes/third-party/umami_analytics", {}, { cache: true })

  if theme.busuanzi.site_uv || theme.busuanzi.site_pv || theme.busuanzi.page_pv
    script(async data-pjax src= theme.asset.busuanzi || '//busuanzi.ibruce.info/busuanzi/2.3/busuanzi.pure.mini.js')

  != partial('includes/third-party/search/index', {}, { cache: true })
```

### 文件路径: `themes\butterfly\layout\includes\footer.pug`
```pug
#footer-wrap
  if theme.footer.owner.enable
    - const currentYear = new Date().getFullYear()
    - const sinceYear = theme.footer.owner.since
    .copyright
      if sinceYear && sinceYear != currentYear
        != `&copy;${sinceYear} - ${currentYear} By ${config.author}`
      else
        != `&copy;${currentYear} By ${config.author}`
  if theme.footer.copyright
    - const v = getVersion()
    .framework-info
      span= _p('footer.framework') + ' '
      a(href='https://hexo.io')= `Hexo ${v.hexo}`
      span.footer-separator |
      span= _p('footer.theme') + ' '
      a(href='https://github.com/jerryc127/hexo-theme-butterfly')= `Butterfly ${v.theme}`
  if theme.footer.custom_text
    .footer_custom_text!= theme.footer.custom_text
```

### 文件路径: `themes\butterfly\layout\includes\head.pug`
```pug
- var pageTitle
- globalPageType === 'archive' ? page.title = findArchivesTitle(page, theme.menu, date) : ''
case globalPageType
  when 'tag'
    - pageTitle = _p('page.tag') + ': ' + page.tag
  when 'category'
    - pageTitle = _p('page.category') + ': ' + page.category
  when '404'
    - pageTitle = _p('error404')
  default
    - pageTitle = page.seo_title || page.title || config.title || ''


- var isSubtitle = config.subtitle ? ' - ' + config.subtitle : ''
- var tabTitle = globalPageType === 'home' || !pageTitle ? config.title + isSubtitle : pageTitle + ' | ' + config.title
- var pageAuthor = config.email ? config.author + ',' + config.email : config.author
- var pageCopyright = config.copyright || config.author
- var themeColorLight = theme.theme_color && theme.theme_color.enable && theme.theme_color.meta_theme_color_light || '#ffffff'
- var themeColorDark = theme.theme_color && theme.theme_color.enable && theme.theme_color.meta_theme_color_dark || '#0d0d0d'
- var themeColor = theme.display_mode === 'dark' ? themeColorDark : themeColorLight

meta(charset='UTF-8')
meta(http-equiv="X-UA-Compatible" content="IE=edge")
meta(name="viewport" content="width=device-width, initial-scale=1.0,viewport-fit=cover")
title= tabTitle
meta(name="author" content=pageAuthor)
meta(name="copyright" content=pageCopyright)
meta(name ="format-detection" content="telephone=no")
meta(name="theme-color" content=themeColor)

//- Open_Graph
include ./head/Open_Graph.pug

//- Structured Data
include ./head/structured_data.pug

!=favicon_tag(theme.favicon || config.favicon)
link(rel="canonical" href=urlNoIndex(null,config.pretty_urls.trailing_index,config.pretty_urls.trailing_html))

//- 預解析
!=partial('includes/head/preconnect', {}, {cache: true})

//- 網站驗證
!=partial('includes/head/site_verification', {}, {cache: true})

//- PWA
if (theme.pwa && theme.pwa.enable)
  !=partial('includes/head/pwa', {}, {cache: true})

//- main css
link(rel='stylesheet', href=url_for(theme.asset.main_css))
link(rel='stylesheet', href=url_for(theme.asset.fontawesome))

if (theme.snackbar && theme.snackbar.enable)
  link(rel='stylesheet', href=url_for(theme.asset.snackbar_css) media="print" onload="this.media='all'")

if theme.lightbox === 'fancybox'
  link(rel='stylesheet' href=url_for(theme.asset.fancybox_css) media="print" onload="this.media='all'")

!=fragment_cache('injectHeadJs', function(){return inject_head_js()})

//- google_adsense
!=partial('includes/head/google_adsense', {}, {cache: true})

//- analytics
!=partial('includes/head/analytics', {}, {cache: true})

//- font
if theme.blog_title_font && theme.blog_title_font.font_link
  link(rel='stylesheet' href=url_for(theme.blog_title_font.font_link) media="print" onload="this.media='all'")

//- global config
!=partial('includes/head/config', {}, {cache: true})

include ./head/config_site.pug

!=fragment_cache('injectHead', function(){return injectHtml(theme.inject.head)})

```

### 文件路径: `themes\butterfly\layout\includes\layout.pug`
```pug
- var globalPageType = getPageType(page, is_home)
- var htmlClassHideAside = theme.aside.enable && theme.aside.hide ? 'hide-aside' : ''
- page.aside = globalPageType === 'archive' ? theme.aside.display.archive: globalPageType === 'category' ? theme.aside.display.category : globalPageType === 'tag' ? theme.aside.display.tag : page.aside
- var hideAside = !theme.aside.enable || page.aside === false ? 'hide-aside' : ''
- var pageType = globalPageType === 'post' ? 'post' : 'page'
- pageType = page.type ? pageType + ' type-' + page.type : pageType

doctype html
html(lang=config.language data-theme=theme.display_mode class=htmlClassHideAside)
  head
    include ./head.pug
  body
    !=partial('includes/loading/index', {}, {cache: true})

    if theme.background
      #web_bg(style=getBgPath(theme.background))

    !=partial('includes/sidebar', {}, {cache: true})

    #body-wrap(class=pageType)
      include ./header/index.pug

      main#content-inner.layout(class=hideAside)
        if body
          div!= body
        else
          block content
          if theme.aside.enable && page.aside !== false
            include widget/index.pug

      - const footerBg = theme.footer_img
      - const footer_bg = footerBg ? footerBg === true ? bg_img : getBgPath(footerBg) : ''
      footer#footer(style=footer_bg)
        !=partial('includes/footer', {}, {cache: true})

    include ./rightside.pug
    include ./additional-js.pug
```

### 文件路径: `themes\butterfly\layout\includes\pagination.pug`
```pug
-
  var options = {
    prev_text: '<i class="fas fa-chevron-left fa-fw"></i>',
    next_text: '<i class="fas fa-chevron-right fa-fw"></i>',
    mid_size: 1,
    escape: false
  }

if globalPageType === 'post'
  - let paginationOrder = theme.post_pagination === 1 ? { prev: page.prev, next: page.next } : { prev: page.next, next: page.prev }

  nav#pagination.pagination-post
    each direction, key in paginationOrder
      if direction
        - const getPostDesc = direction.postDesc || postDesc(direction)
        - let className = key === 'prev' ? (paginationOrder.next ? '' : 'full-width') : (paginationOrder.prev ? '' : 'full-width')
        - className = getPostDesc ? className : className + ' no-desc'

        a.pagination-related(class=className href=url_for(direction.path) title=direction.title)
          if direction.cover_type === 'img'
            img.cover(src=url_for(direction.cover) onerror=`onerror=null;src='${url_for(theme.error_img.post_page)}'` alt=`cover of ${key === 'prev' ? 'previous' : 'next'} post`)
          else
            .cover(style=`background: ${direction.cover || 'var(--default-bg-color)'}`)

          .info(class=key === 'prev' ? '' : 'text-right')
            .info-1
              .info-item-1=_p(`pagination.${key}`)
              .info-item-2!=direction.title
            if getPostDesc
              .info-2
                .info-item-1!=getPostDesc
else
  nav#pagination
    .pagination
      if globalPageType === 'home'
        - options.format = 'page/%d/#content-inner'
      !=paginator(options)
```

### 文件路径: `themes\butterfly\layout\includes\rightside.pug`
```pug
- const { readmode, translate, darkmode, aside, chat } = theme
mixin rightsideItem(array)
  each item in array
    case item
      when 'readmode'
        if globalPageType === 'post' && readmode
          button#readmode(type="button" title=_p('rightside.readmode_title'))
            i.fas.fa-book-open
      when 'translate'
        if translate.enable
          button#translateLink(type="button" title=_p('rightside.translate_title'))= translate.default
      when 'darkmode'
        if darkmode.enable && darkmode.button
          button#darkmode(type="button" title=_p('rightside.night_mode_title'))
            i.fas.fa-adjust
      when 'hideAside'
        if aside.enable && aside.button && page.aside !== false
          button#hide-aside-btn(type="button" title=_p('rightside.aside'))
            i.fas.fa-arrows-alt-h
      when 'toc'
        if showToc
          button#mobile-toc-button.close(type="button" title=_p("rightside.toc"))
            i.fas.fa-list-ul
      when 'chat'
        if chat.rightside_button && chat.use
          button#chat-btn(type="button" title=_p("rightside.chat") style="display:none")
            i.fas.fa-message
      when 'comment'
        if commentsJsLoad
          a#to_comment(href="#post-comment" title=_p("rightside.scroll_to_comment"))
            i.fas.fa-comments

#rightside
  - const { enable, hide, show } = theme.rightside_item_order
  - const hideArray = enable ? hide && hide.split(',') : ['readmode','translate','darkmode','hideAside']
  - const showArray = enable ? show && show.split(',') : ['toc','chat','comment']


  #rightside-config-hide
    if hideArray
      +rightsideItem(hideArray)
  #rightside-config-show
    if enable
      if hide
        button#rightside-config(type="button" title=_p("rightside.setting"))
          i.fas.fa-cog.fa-spin
    else
      if globalPageType === 'post'
        if (readmode || translate.enable || (darkmode.enable && darkmode.button))
          button#rightside-config(type="button" title=_p("rightside.setting"))
            i.fas.fa-cog.fa-spin
      else if translate.enable || (darkmode.enable && darkmode.button)
        button#rightside-config(type="button" title=_p("rightside.setting"))
          i.fas.fa-cog.fa-spin

    if showArray
      +rightsideItem(showArray)

    button#go-up(type="button" title=_p("rightside.back_to_top"))
      span.scroll-percent
      i.fas.fa-arrow-up
```

### 文件路径: `themes\butterfly\layout\includes\sidebar.pug`
```pug
if theme.menu
  #sidebar
    #menu-mask
    #sidebar-menus
      .avatar-img.text-center
        img(src=url_for(theme.avatar.img) onerror=`this.onerror=null;this.src='${url_for(theme.error_img.flink)}'` alt="avatar")
      .site-data.text-center
        a(href=`${url_for(config.archive_dir)}/`)
          .headline= _p('aside.articles')
          .length-num= site.posts.length
        a(href=`${url_for(config.tag_dir)}/`)
          .headline= _p('aside.tags')
          .length-num= site.tags.length
        a(href=`${url_for(config.category_dir)}/`)
          .headline= _p('aside.categories')
          .length-num= site.categories.length

      != partial('includes/header/menu_item', {}, { cache: true })
```

### 文件路径: `themes\butterfly\layout\includes\head\Open_Graph.pug`
```pug
if theme.Open_Graph_meta.enable
  -
    const coverVal = page.cover_type === 'img' ? page.cover : theme.avatar.img
    let ogOption = Object.assign({
      type: globalPageType === 'post' ? 'article' : 'website',
      image: coverVal ? full_url_for(coverVal) : '',
      fb_admins: theme.facebook_comments.user_id || '',
      fb_app_id: theme.facebook_comments.app_id || '',
    }, theme.Open_Graph_meta.option)
  -
  != open_graph(ogOption)
else
  - const description = page.description || page.content || page.title || config.description
  if description
    meta(name="description" content=truncate(description, 150))


```

### 文件路径: `themes\butterfly\layout\includes\head\analytics.pug`
```pug
if theme.baidu_analytics
  script.
    var _hmt = _hmt || [];
    (function() {
      var hm = document.createElement("script");
      hm.src = "https://hm.baidu.com/hm.js?!{theme.baidu_analytics}";
      var s = document.getElementsByTagName("script")[0];
      s.parentNode.insertBefore(hm, s);
    })();
    btf.addGlobalFn('pjaxComplete', () => {
      _hmt.push(['_trackPageview',window.location.pathname])
    }, 'baidu_analytics')

if theme.google_analytics
  script(async src=`https://www.googletagmanager.com/gtag/js?id=${theme.google_analytics}`)
  script.
    window.dataLayer = window.dataLayer || []
    function gtag(){dataLayer.push(arguments)}
    gtag('js', new Date())
    gtag('config', '!{theme.google_analytics}')
    btf.addGlobalFn('pjaxComplete', () => {
      gtag('config', '!{theme.google_analytics}', {'page_path': window.location.pathname})
    }, 'google_analytics')

if theme.cloudflare_analytics
  script(defer data-pjax src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon=`{"token": "${theme.cloudflare_analytics}"}`)

if theme.microsoft_clarity
  script.
    (function(c,l,a,r,i,t,y){
        c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};
        t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
        y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
    })(window, document, "clarity", "script", "!{theme.microsoft_clarity}");
```

### 文件路径: `themes\butterfly\layout\includes\head\config.pug`
```pug
-
  let algolia = 'undefined'
  if (theme.search.use === 'algolia_search') {
    const { ALGOLIA_APP_ID, ALGOLIA_API_KEY, ALGOLIA_INDEX_NAME } = process.env
    const { appId, applicationID, apiKey, indexName } = config.algolia
    algolia = JSON.stringify({
      appId: ALGOLIA_APP_ID || appId || applicationID,
      apiKey: ALGOLIA_API_KEY || apiKey,
      indexName: ALGOLIA_INDEX_NAME || indexName,
      hitsPerPage: theme.search.algolia_search.hitsPerPage,
      // search languages
      languages: {
        input_placeholder: theme.search.placeholder || _p("search.input_placeholder"),
        hits_empty: _p("search.algolia_search.hits_empty"),
        hits_stats: _p("search.algolia_search.hits_stats"),
      }
    })
  }

  let localSearch = 'undefined'
  if (theme.search.use === 'local_search') {
    const { CDN, preload, top_n_per_article, unescape } = theme.search.local_search
    localSearch = JSON.stringify({
      path: CDN || config.root + config.search.path,
      preload,
      top_n_per_article,
      unescape,
      languages: {
        // search languages
        hits_empty: _p("search.local_search.hits_empty"),
        hits_stats: _p("search.local_search.hits_stats"),
      }
    })
  }

  let translate = 'undefined'
  if (theme.translate && theme.translate.enable){
    translate = JSON.stringify({
      defaultEncoding: theme.translate.defaultEncoding,
      translateDelay: theme.translate.translateDelay,
      msgToTraditionalChinese: theme.translate.msgToTraditionalChinese,
      msgToSimplifiedChinese: theme.translate.msgToSimplifiedChinese
    })
  }

  let copyright = 'undefined'
  if (theme.copy.enable && theme.copy.copyright.enable){
    copyright = JSON.stringify({
      limitCount: theme.copy.copyright.limit_count,
      languages: {
        author: _p("copy_copyright.author") + ': ' + config.author,
        link: _p("copy_copyright.link") + ': ',
        source: _p("copy_copyright.source") + ': ' + config.title,
        info: _p("copy_copyright.info")
      }
    })
  }

  let Snackbar = 'undefined'
  if (theme.snackbar && theme.snackbar.enable) {
    Snackbar = JSON.stringify({
      chs_to_cht: _p("Snackbar.chs_to_cht"),
      cht_to_chs: _p("Snackbar.cht_to_chs"),
      day_to_night: _p("Snackbar.day_to_night"),
      night_to_day: _p("Snackbar.night_to_day"),
      bgLight: theme.snackbar.bg_light,
      bgDark: theme.snackbar.bg_dark,
      position: theme.snackbar.position,
    })
  }

  let highlight = 'undefined'
  let syntaxHighlighter = config.syntax_highlighter
  let highlightEnable = syntaxHighlighter ? ['highlight.js', 'prismjs'].includes(syntaxHighlighter) : (config.highlight.enable || config.prismjs.enable)
  if (highlightEnable) {
    const { copy, language, height_limit, fullpage, macStyle } = theme.code_blocks
    highlight = JSON.stringify({
      plugin: syntaxHighlighter ? syntaxHighlighter : config.highlight.enable ? 'highlight.js' : 'prismjs',
      highlightCopy: copy,
      highlightLang: language,
      highlightHeightLimit: height_limit,
      highlightFullpage: fullpage,
      highlightMacStyle: macStyle
    })
  }

script.
  const GLOBAL_CONFIG = {
    root: '!{config.root}',
    algolia: !{algolia},
    localSearch: !{localSearch},
    translate: !{translate},
    highlight: !{highlight},
    copy: {
      success: '!{_p("copy.success")}',
      error: '!{_p("copy.error")}',
      noSupport: '!{_p("copy.noSupport")}'
    },
    relativeDate: {
      homepage: !{theme.post_meta.page.date_format === 'relative'},
      post: !{theme.post_meta.post.date_format === 'relative'}
    },
    runtime: '!{theme.aside.card_webinfo.runtime_date ? _p("aside.card_webinfo.runtime.unit") : ""}',
    dateSuffix: {
      just: '!{_p("date_suffix.just")}',
      min: '!{_p("date_suffix.min")}',
      hour: '!{_p("date_suffix.hour")}',
      day: '!{_p("date_suffix.day")}',
      month: '!{_p("date_suffix.month")}'
    },
    copyright: !{copyright},
    lightbox: '!{ theme.lightbox || 'null' }',
    Snackbar: !{Snackbar},
    infinitegrid: {
      js: '!{url_for(theme.asset.egjs_infinitegrid)}',
      buttonText: '!{_p("load_more")}'
    },
    isPhotoFigcaption: !{theme.photofigcaption},
    islazyloadPlugin: !{theme.lazyload.enable && !theme.lazyload.native},
    isAnchor: !{theme.anchor.auto_update || false},
    percent: {
      toc: !{theme.toc.scroll_percent},
      rightside: !{theme.rightside_scroll_percent},
    },
    autoDarkmode: !{theme.darkmode.enable && theme.darkmode.autoChangeMode === 1}
  }

```

### 文件路径: `themes\butterfly\layout\includes\head\config_site.pug`
```pug
-
  const titleVal = pageTitle.replace(/'/ig,"\\'")

  let isHighlightShrink
  if (theme.code_blocks.shrink == 'none') isHighlightShrink = 'undefined'
  else if (typeof page.highlight_shrink == 'boolean') isHighlightShrink = page.highlight_shrink
  else isHighlightShrink = theme.code_blocks.shrink

  var showToc = false
  if (theme.aside.enable && page.aside !== false) {
    let tocEnable = false
    if (globalPageType === 'post' && theme.toc.post) tocEnable = true
    else if (globalPageType === 'page' && theme.toc.page) tocEnable = true
    const pageToc = typeof page.toc === 'boolean' ? page.toc : tocEnable
    showToc = pageToc && (toc(page.content) !== '' || page.encrypt === true)
  }
-

script#config-diff.
  var GLOBAL_CONFIG_SITE = {
    title: '!{titleVal}',
    isHighlightShrink: !{isHighlightShrink},
    isToc: !{showToc},
    pageType: '!{page.type == 'shuoshuo' ? 'shuoshuo' : globalPageType}'
  }

```

### 文件路径: `themes\butterfly\layout\includes\head\google_adsense.pug`
```pug
if (theme.google_adsense && theme.google_adsense.enable)
  script(async src=theme.google_adsense.js)

  if theme.google_adsense.auto_ads
    script.
      (adsbygoogle = window.adsbygoogle || []).push({
        google_ad_client: '!{theme.google_adsense.client}',
        enable_page_level_ads: '!{theme.google_adsense.enable_page_level_ads}'
      });
```

### 文件路径: `themes\butterfly\layout\includes\head\preconnect.pug`
```pug
-
  const { internal_provider, third_party_provider, custom_format } = theme.CDN
  const providers = {
    'jsdelivr': '//cdn.jsdelivr.net',
    'cdnjs': '//cdnjs.cloudflare.com',
    'unpkg': '//unpkg.com',
    'custom': custom_format && custom_format.match(/^((https?:)?(\/\/[^/]+)|([^/]+))(\/|$)/)[1]
  }
-

if internal_provider === third_party_provider && internal_provider !== 'local'
  link(rel="preconnect" href=providers[internal_provider])
else
  if internal_provider !== 'local'
    link(rel="preconnect" href=providers[internal_provider])
  if third_party_provider !== 'local'
  link(rel="preconnect" href=providers[third_party_provider])

if theme.google_analytics
  link(rel="preconnect" href="//www.google-analytics.com" crossorigin='')

if theme.baidu_analytics
  link(rel="preconnect" href="//hm.baidu.com")

if theme.cloudflare_analytics
  link(rel="preconnect" href="//static.cloudflareinsights.com")

if theme.microsoft_clarity
  link(rel="preconnect" href="//www.clarity.ms")

if theme.blog_title_font && theme.blog_title_font.font_link && theme.blog_title_font.font_link.indexOf('//fonts.googleapis.com') != -1
  link(rel="preconnect" href="//fonts.googleapis.com" crossorigin='')

if !theme.asset.busuanzi && (theme.busuanzi.site_uv || theme.busuanzi.site_pv || theme.busuanzi.page_pv)
  link(rel="preconnect" href="//busuanzi.ibruce.info")
```

### 文件路径: `themes\butterfly\layout\includes\head\pwa.pug`
```pug
- const { manifest, theme_color, apple_touch_icon, favicon_32_32, favicon_16_16, mask_icon } = theme.pwa

link(rel="manifest" href=url_for(manifest))
if theme_color
  meta(name="msapplication-TileColor" content=theme_color)
if apple_touch_icon
  link(rel="apple-touch-icon" sizes="180x180" href=url_for(apple_touch_icon))
if favicon_32_32
  link(rel="icon" type="image/png" sizes="32x32" href=url_for(favicon_32_32))
if favicon_16_16
  link(rel="icon" type="image/png" sizes="16x16" href=url_for(favicon_16_16))
if mask_icon
  link(rel="mask-icon" href=url_for(mask_icon) color="#5bbad5")

```

### 文件路径: `themes\butterfly\layout\includes\head\site_verification.pug`
```pug
if theme.site_verification
  each item in theme.site_verification
    meta(name=item.name content=item.content)
```

### 文件路径: `themes\butterfly\layout\includes\head\structured_data.pug`
```pug
if theme.structured_data && page.layout === 'post'
  -
    // use json-ld to add structured data

    const title = page.title
    const url = page.permalink
    const imageVal = page.cover_type === 'img' ? page.cover : theme.avatar.img
    const image = imageVal ? full_url_for(imageVal) : ''
    const datePublished = page.date.toISOString()
    const dateModified = (page.updated || page.date).toISOString()
    const author = page.copyright_author || config.author
    const authorHrefVal = page.copyright_author_href || theme.post_copyright.author_href || site.url;
    const authorHref = full_url_for(authorHrefVal);

    const jsonLd = {
      "@context": "https://schema.org",
      "@type": "BlogPosting",
      "headline": title,
      "url": url,
      "image": image,
      "datePublished": datePublished,
      "dateModified": dateModified,
      "author": [{
        "@type": "Person",
        "name": author,
        "url": authorHref
      }]
    };

    jsonLdScript = JSON.stringify(jsonLd, null, 2);
  -

  script(type="application/ld+json").
    !{jsonLdScript}

```

### 文件路径: `themes\butterfly\layout\includes\header\index.pug`
```pug
-
  const returnTopImg = img => img !== false ? img || theme.default_top_img : false
  const isFixedClass = theme.nav.fixed ? ' fixed' : ''
  var top_img = false
  let headerClassName = 'not-top-img'
  var bg_img = ''

if !theme.disable_top_img && page.top_img !== false
  case globalPageType
    when 'post'
      - top_img = page.top_img || page.cover || theme.default_top_img
    when 'page'
      - top_img = page.top_img || theme.default_top_img
    when 'tag'
      - top_img = theme.tag_per_img && theme.tag_per_img[page.tag] || returnTopImg(theme.tag_img)
    when 'category'
      - top_img = theme.category_per_img && theme.category_per_img[page.category] || returnTopImg(theme.category_img)
    when 'home'
      - top_img = returnTopImg(theme.index_img)
    when 'archive'
      - top_img = returnTopImg(theme.archive_img)
    default
      - top_img = page.top_img || theme.default_top_img

  if top_img !== false
    - bg_img = getBgPath(top_img)
    - headerClassName = globalPageType === 'home' ? 'full_page' : globalPageType === 'post' ? 'post-bg' : 'not-home-page'

header#page-header(class=`${headerClassName + isFixedClass}` style=bg_img)
  include ./nav.pug
  if top_img !== false
    if globalPageType === 'post'
      include ./post-info.pug
    else if globalPageType === 'home'
      #site-info
        h1#site-title=config.title
        if theme.subtitle.enable
          - var loadSubJs = true
          #site-subtitle
            span#subtitle
        if theme.social
          #site_social_icons
            !=partial('includes/header/social', {}, {cache: true})
      #scroll-down
        i.fas.fa-angle-down.scroll-down-effects
    else
      #page-site-info
        h1#site-title=page.title || page.tag || page.category
  else
    //- improve seo
    if globalPageType !== 'post'
      h1.title-seo=page.title || page.tag || page.category || config.title
```

### 文件路径: `themes\butterfly\layout\includes\header\menu_item.pug`
```pug
if theme.menu
  .menus_items
    each value, label in theme.menu
      if typeof value !== 'object'
        .menus_item
          - const [link, icon] = value.split('||').map(part => trim(part))
          a.site-page(href=url_for(link))
            if icon
              i.fa-fw(class=icon)
            span= ' ' + label
      else
        .menus_item
          - const [groupLabel, groupIcon, groupClass] = label.split('||').map(part => trim(part))
          - const hideClass = groupClass === 'hide' ? 'hide' : ''
          span.site-page.group(class=hideClass)
            if groupIcon
              i.fa-fw(class=groupIcon)
            span= ' ' + groupLabel
            i.fas.fa-chevron-down
          ul.menus_item_child
            each val, lab in value
              - const [childLink, childIcon] = val.split('||').map(part => trim(part))
              li
                a.site-page.child(href=url_for(childLink))
                  if childIcon
                    i.fa-fw(class=childIcon)
                  span= ' ' + lab
```

### 文件路径: `themes\butterfly\layout\includes\header\nav.pug`
```pug
nav#nav
  span#blog-info
    a.nav-site-title(href=url_for('/'))
      if theme.nav.logo
        img.site-icon(src=url_for(theme.nav.logo) alt='Logo')
      if theme.nav.display_title
        span.site-name=config.title
    if globalPageType === 'post'
      a.nav-page-title(href=url_for('/'))
        span.site-name=(page.title || config.title)
  #menus
    if theme.search.use
      #search-button
        span.site-page.social-icon.search
          i.fas.fa-search.fa-fw
          span= ' ' + _p('search.title')
    if theme.menu
      != partial('includes/header/menu_item', {}, {cache: true})

      #toggle-menu
        span.site-page
          i.fas.fa-bars.fa-fw
```

### 文件路径: `themes\butterfly\layout\includes\header\post-info.pug`
```pug
- let comments = theme.comments
#post-info
  h1.post-title= page.title || _p('no_title')
    if theme.post_edit.enable
      a.post-edit-link(href=theme.post_edit.url + page.source title=_p('post.edit') target="_blank")
        i.fas.fa-pencil-alt

  #post-meta
    .meta-firstline
      if theme.post_meta.post.date_type
        span.post-meta-date
          if theme.post_meta.post.date_type === 'both'
            i.far.fa-calendar-alt.fa-fw.post-meta-icon
            span.post-meta-label= _p('post.created')
            time.post-meta-date-created(datetime=date_xml(page.date) title=_p('post.created') + ' ' + full_date(page.date))= date(page.date, config.date_format)
            span.post-meta-separator |
            i.fas.fa-history.fa-fw.post-meta-icon
            span.post-meta-label= _p('post.updated')
            time.post-meta-date-updated(datetime=date_xml(page.updated) title=_p('post.updated') + ' ' + full_date(page.updated))= date(page.updated, config.date_format)
          else
            - let data_type_update = theme.post_meta.post.date_type === 'updated'
            - let date_type = data_type_update ? 'updated' : 'date'
            - let date_icon = data_type_update ? 'fas fa-history' : 'far fa-calendar-alt'
            - let date_title = data_type_update ? _p('post.updated') : _p('post.created')
            i.fa-fw.post-meta-icon(class=date_icon)
            span.post-meta-label= date_title
            time(datetime=date_xml(page[date_type]) title=date_title + ' ' + full_date(page[date_type]))= date(page[date_type], config.date_format)
      if theme.post_meta.post.categories && page.categories.data.length > 0
        span.post-meta-categories
          if theme.post_meta.post.date_type
            span.post-meta-separator |
          each item, index in page.categories.data
            i.fas.fa-inbox.fa-fw.post-meta-icon
            a(href=url_for(item.path)).post-meta-categories #[=item.name]
            if index < page.categories.data.length - 1
              i.fas.fa-angle-right.post-meta-separator

    .meta-secondline
      - let postWordcount = theme.wordcount.enable && (theme.wordcount.post_wordcount || theme.wordcount.min2read)
      if postWordcount
        span.post-meta-separator |
        span.post-meta-wordcount
          if theme.wordcount.post_wordcount
            i.far.fa-file-word.fa-fw.post-meta-icon
            span.post-meta-label= _p('post.wordcount') + ':'
            span.word-count= wordcount(page.content)
            if theme.wordcount.min2read
              span.post-meta-separator |
          if theme.wordcount.min2read
            i.far.fa-clock.fa-fw.post-meta-icon
            span.post-meta-label= _p('post.min2read') + ':'
            span= min2read(page.content, {cn: 350, en: 160}) + _p('post.min2read_unit')

      //- for pv and count
      mixin pvBlock(parent_id, parent_class, parent_title)
        span.post-meta-separator |
        span(class=parent_class id=parent_id data-flag-title=parent_title)
          i.far.fa-eye.fa-fw.post-meta-icon
          span.post-meta-label= _p('post.page_pv') + ':'
          if block
            block

      mixin otherPV()
        if theme.umami_analytics.enable && theme.umami_analytics.UV_PV.page_pv
          +pvBlock('', '', '')
            span#umamiPV(data-path=url_for(page.path))
              i.fa-solid.fa-spinner.fa-spin
        else if theme.busuanzi.page_pv
          +pvBlock('', 'post-meta-pv-cv', '')
            span#busuanzi_value_page_pv
              i.fa-solid.fa-spinner.fa-spin

      - const commentUse = comments.use && comments.use[0]
      if page.comments !== false && commentUse && !comments.lazyload
        if commentUse === 'Valine' && theme.valine.visitor
          +pvBlock(url_for(page.path), 'leancloud_visitors', page.title)
            span.leancloud-visitors-count
              i.fa-solid.fa-spinner.fa-spin
        else if commentUse === 'Waline' && theme.waline.pageview
          +pvBlock('', '', '')
            span.waline-pageview-count(data-path=url_for(page.path))
              i.fa-solid.fa-spinner.fa-spin
        else if commentUse === 'Twikoo' && theme.twikoo.visitor
          +pvBlock('', '', '')
            span#twikoo_visitors
              i.fa-solid.fa-spinner.fa-spin
        else if commentUse === 'Artalk' && theme.artalk.visitor
          +pvBlock('', '', '')
            span#ArtalkPV
              i.fa-solid.fa-spinner.fa-spin
        else
          +otherPV()
      else
        +otherPV()

      if comments.count && !comments.lazyload && page.comments !== false && comments.use
        - var whichCount = comments.use[0]

        mixin countBlock
          span.post-meta-separator |
          span.post-meta-commentcount
            i.far.fa-comments.fa-fw.post-meta-icon
            span.post-meta-label= _p('post.comments') + ':'
            if block
              block

        case whichCount
          when 'Disqus'
            +countBlock
              a.disqus-comment-count(href=full_url_for(page.path) + '#post-comment')
                i.fa-solid.fa-spinner.fa-spin
          when 'Disqusjs'
            +countBlock
              a.disqusjs-comment-count(href=full_url_for(page.path) + '#post-comment')
                i.fa-solid.fa-spinner.fa-spin
          when 'Valine'
            +countBlock
              a(href=url_for(page.path) + '#post-comment' itemprop="discussionUrl")
                span.valine-comment-count(data-xid=url_for(page.path) itemprop="commentCount")
                  i.fa-solid.fa-spinner.fa-spin
          when 'Waline'
            +countBlock
              a(href=url_for(page.path) + '#post-comment')
                span.waline-comment-count(data-path=url_for(page.path))
                  i.fa-solid.fa-spinner.fa-spin
          when 'Gitalk'
            +countBlock
              a(href=url_for(page.path) + '#post-comment')
                span.gitalk-comment-count
                  i.fa-solid.fa-spinner.fa-spin
          when 'Twikoo'
            +countBlock
              a(href=url_for(page.path) + '#post-comment')
                span#twikoo-count
                  i.fa-solid.fa-spinner.fa-spin
          when 'Facebook Comments'
            +countBlock
              a(href=url_for(page.path) + '#post-comment')
                span.fb-comments-count(data-href=urlNoIndex())
          when 'Remark42'
            +countBlock
              a(href=url_for(page.path) + '#post-comment')
                span.remark42__counter(data-url=urlNoIndex())
                  i.fa-solid.fa-spinner.fa-spin
          when 'Artalk'
            +countBlock
              a(href=url_for(page.path) + '#post-comment')
                span#ArtalkCount
                  i.fa-solid.fa-spinner.fa-spin
```

### 文件路径: `themes\butterfly\layout\includes\header\social.pug`
```pug
each url, icon in theme.social
  -
    const [link, title, color] = url.split('||').map(i => trim(i))
    const href = url_for(link)
    const iconStyle = color ? `color: ${color.replace(/[\'\"]/g, '')};` : ''
    const iconTitle = title || ''
  a.social-icon(href=href target="_blank" title=iconTitle)
    i(class=icon style=iconStyle)
```

### 文件路径: `themes\butterfly\layout\includes\loading\fullpage-loading.pug`
```pug
#loading-box
  .loading-left-bg
  .loading-right-bg
  .spinner-box
    .configure-border-1
      .configure-core
    .configure-border-2
      .configure-core
    .loading-word= _p('loading')

script.
  (()=>{
    const $loadingBox = document.getElementById('loading-box')
    const $body = document.body
    const preloader = {
      endLoading: () => {
        $body.style.overflow = ''
        $loadingBox.classList.add('loaded')
      },
      initLoading: () => {
        $body.style.overflow = 'hidden'
        $loadingBox.classList.remove('loaded')
      }
    }

    preloader.initLoading()
    window.addEventListener('load', preloader.endLoading)

    if (!{theme.pjax && theme.pjax.enable}) {
      btf.addGlobalFn('pjaxSend', preloader.initLoading, 'preloader_init')
      btf.addGlobalFn('pjaxComplete', preloader.endLoading, 'preloader_end')
    }
  })()
```

### 文件路径: `themes\butterfly\layout\includes\loading\index.pug`
```pug
if theme.preloader.enable
  if theme.preloader.source === 1
    include ./fullpage-loading.pug
  else
    include ./pace.pug
```

### 文件路径: `themes\butterfly\layout\includes\loading\pace.pug`
```pug
script.
  window.paceOptions = {
    restartOnPushState: false
  }

  btf.addGlobalFn('pjaxSend', () => {
    Pace.restart()
  }, 'pace_restart')


link(rel="stylesheet", href=url_for(theme.preloader.pace_css_url || theme.asset.pace_default_css))
script(src=url_for(theme.asset.pace_js))
```

### 文件路径: `themes\butterfly\layout\includes\mixins\article-sort.pug`
```pug
mixin articleSort(posts)
  .article-sort
    - let year
    - posts.forEach(article => {
      - const tempYear = date(article.date, 'YYYY')
      - const noCoverClass = article.cover === false || !theme.cover.archives_enable ? 'no-article-cover' : ''
      - const title = article.title || _p('no_title')
      if tempYear !== year
        - year = tempYear
        .article-sort-item.year= year
      .article-sort-item(class=noCoverClass)
        if article.cover && theme.cover.archives_enable
          a.article-sort-item-img(href=url_for(article.path) title=title)
            if article.cover_type === 'img'
              img(src=url_for(article.cover) alt=title onerror=`this.onerror=null;this.src='${url_for(theme.error_img.post_page)}'`)
            else
              div(style=`background: ${article.cover}`)
        .article-sort-item-info
          .article-sort-item-time
            i.far.fa-calendar-alt
            time.post-meta-date-created(datetime=date_xml(article.date) title=_p('post.created') + ' ' + full_date(article.date))= date(article.date, config.date_format)
          a.article-sort-item-title(href=url_for(article.path) title=title)= title
    - })
```

### 文件路径: `themes\butterfly\layout\includes\mixins\indexPostUI.pug`
```pug
mixin indexPostUI()
  - const indexLayout = theme.index_layout
  - const masonryLayoutClass = (indexLayout === 6 || indexLayout === 7) ? 'masonry' : ''
  #recent-posts.recent-posts.nc(class=masonryLayoutClass)
    .recent-post-items
      each article, index in page.posts.data
        .recent-post-item
          - const link = article.link || article.path
          - const title = article.title || _p('no_title')
          - const leftOrRight = indexLayout === 3 ? (index % 2 === 0 ? 'left' : 'right') : (indexLayout === 2 ? 'right' : '')
          - const post_cover = article.cover
          - const no_cover = article.cover === false || !theme.cover.index_enable ? 'no-cover' : ''

          if post_cover && theme.cover.index_enable
            .post_cover(class=leftOrRight)
              a(href=url_for(link) title=title)
                if article.cover_type === 'img'
                  img.post-bg(src=url_for(post_cover) onerror=`this.onerror=null;this.src='${url_for(theme.error_img.post_page)}'` alt=title)
                else
                  div.post-bg(style=`background: ${post_cover}`)
          .recent-post-info(class=no_cover)
            a.article-title(href=url_for(link) title=title)
              if globalPageType === 'home' && (article.top || article.sticky > 0)
                i.fas.fa-thumbtack.sticky
              = title
            .article-meta-wrap
              if theme.post_meta.page.date_type
                span.post-meta-date
                  if theme.post_meta.page.date_type === 'both'
                    i.far.fa-calendar-alt
                    span.article-meta-label=_p('post.created')
                    time.post-meta-date-created(datetime=date_xml(article.date) title=_p('post.created') + ' ' + full_date(article.date))= date(article.date, config.date_format)
                    span.article-meta-separator |
                    i.fas.fa-history
                    span.article-meta-label=_p('post.updated')
                    time.post-meta-date-updated(datetime=date_xml(article.updated) title=_p('post.updated') + ' ' + full_date(article.updated))= date(article.updated, config.date_format)
                  else
                    - const data_type_updated = theme.post_meta.page.date_type === 'updated'
                    - const date_type = data_type_updated ? 'updated' : 'date'
                    - const date_icon = data_type_updated ? 'fas fa-history' : 'far fa-calendar-alt'
                    - const date_title = data_type_updated ? _p('post.updated') : _p('post.created')
                    i(class=date_icon)
                    span.article-meta-label= date_title
                    time(datetime=date_xml(article[date_type]) title=date_title + ' ' + full_date(article[date_type]))= date(article[date_type], config.date_format)
              if theme.post_meta.page.categories && article.categories.data.length > 0
                span.article-meta
                  span.article-meta-separator |
                  each item, index in article.categories.data
                    i.fas.fa-inbox
                    a(href=url_for(item.path)).article-meta__categories #[=item.name]
                    if index < article.categories.data.length - 1
                      i.fas.fa-angle-right.article-meta-link
              if theme.post_meta.page.tags && article.tags.length > 0
                span.article-meta.tags
                  span.article-meta-separator |
                  each item, index in article.tags.data
                    i.fas.fa-tag
                    a(href=url_for(item.path)).article-meta__tags #[=item.name]
                    if index < article.tags.data.length - 1
                      span.article-meta-link #[='•']

              mixin countBlockInIndex
                - needLoadCountJs = true
                span.article-meta
                  span.article-meta-separator |
                  i.fas.fa-comments
                  if block
                    block
                  span.article-meta-label= ' ' + _p('card_post_count')

              if theme.comments.card_post_count && theme.comments.use
                case theme.comments.use[0]
                  when 'Disqus'
                  when 'Disqusjs'
                    +countBlockInIndex
                      a.disqus-count(href=full_url_for(link) + '#post-comment')
                        i.fa-solid.fa-spinner.fa-spin
                  when 'Valine'
                    +countBlockInIndex
                      a(href=url_for(link) + '#post-comment')
                        span.valine-comment-count(data-xid=url_for(link))
                          i.fa-solid.fa-spinner.fa-spin
                  when 'Waline'
                    +countBlockInIndex
                      a(href=url_for(link) + '#post-comment')
                        span.waline-comment-count(data-path=url_for(link))
                          i.fa-solid.fa-spinner.fa-spin
                  when 'Twikoo'
                    +countBlockInIndex
                      a.twikoo-count(href=url_for(link) + '#post-comment')
                        i.fa-solid.fa-spinner.fa-spin
                  when 'Facebook Comments'
                    +countBlockInIndex
                      a(href=url_for(link) + '#post-comment')
                        span.fb-comments-count(data-href=urlNoIndex(article.permalink))
                  when 'Remark42'
                    +countBlockInIndex
                      a(href=url_for(link) + '#post-comment')
                        span.remark42__counter(data-url=urlNoIndex(article.permalink))
                          i.fa-solid.fa-spinner.fa-spin
                  when 'Artalk'
                    +countBlockInIndex
                      a(href=url_for(link) + '#post-comment')
                        span.artalk-count(data-page-key=url_for(link))
                          i.fa-solid.fa-spinner.fa-spin

            //- Display the article introduction on homepage
            - const content = postDesc(article)
            if content
              .content!=content

        if theme.ad && theme.ad.index
          if (index + 1) % 3 === 0
            .recent-post-item.ads-wrap!= theme.ad.index

    include ../pagination.pug
```

### 文件路径: `themes\butterfly\layout\includes\page\404.pug`
```pug
- var top_img_404 = theme.error_404.background || theme.default_top_img

.error-content
  .error-img
    img(src=url_for(top_img_404) alt='Page not found')
  .error-info
    h1.error_title= '404'
    .error_subtitle= theme.error_404.subtitle || _p('error404')

```

### 文件路径: `themes\butterfly\layout\includes\page\categories.pug`
```pug
.category-lists!= list_categories()
```

### 文件路径: `themes\butterfly\layout\includes\page\default-page.pug`
```pug
#article-container.container
  != page.content
```

### 文件路径: `themes\butterfly\layout\includes\page\flink.pug`
```pug
#article-container.container
  .flink
    - let { content, random, flink_url } = page
    - let pageContent = content

    if flink_url || random
      - const linkData = flink_url ? false : site.data.link || false
      script.
        (()=>{
          const replaceSymbol = (str) => {
            return str.replace(/[\p{P}\p{S}]/gu, "-")
          }

          let result = ""
          const add = (str) => {
            for(let i = 0; i < str.length; i++){
              const replaceClassName = replaceSymbol(str[i].class_name)
              const className = str[i].class_name ? `<h2 id="${replaceClassName}"><a href="#${replaceClassName}" class="headerlink" title="${str[i].class_name}"></a>${str[i].class_name}</h2>` : ""
              const classDesc = str[i].class_desc ? `<div class="flink-desc">${str[i].class_desc}</div>` : ""

              let listResult = ""
              const lists = str[i].link_list
              if (!{random === true}) {
                lists.sort(() => Math.random() - 0.5)
              }
              for(let j = 0; j < lists.length; j++){
                listResult += `
                  <div class="flink-list-item">
                    <a href="${lists[j].link}" title="${lists[j].name}" target="_blank">
                      <div class="flink-item-icon">
                        <img class="no-lightbox" src="${lists[j].avatar}" onerror='this.onerror=null;this.src="!{url_for(theme.error_img.flink)}"' alt="${lists[j].name}" />
                      </div>
                      <div class="flink-item-name">${lists[j].name}</div>
                      <div class="flink-item-desc" title="${lists[j].descr}">${lists[j].descr}</div>
                    </a>
                  </div>`
              }

              result += `${className}${classDesc} <div class="flink-list">${listResult}</div>`
            }

            document.querySelector(".flink").insertAdjacentHTML("afterbegin", result)
            window.lazyLoadInstance && window.lazyLoadInstance.update()
          }

          const linkData = !{JSON.stringify(linkData)}
          if (!{Boolean(flink_url)}) {
            fetch("!{url_for(flink_url)}")
              .then(response => response.json())
              .then(add)
          } else if (linkData) {
            add(linkData)
          }
        })()

    else
      if site.data.link
        - let result = ""
        each i in site.data.link
          - let className = i.class_name ? markdown(`## ${i.class_name}`) : ""
          - let classDesc = i.class_desc ? `<div class="flink-desc">${i.class_desc}</div>` : ""

          - let listResult = ""

          each j in i.link_list
            -
              listResult += `
                <div class="flink-list-item">
                  <a href="${j.link}" title="${j.name}" target="_blank">
                    <div class="flink-item-icon">
                      <img class="no-lightbox" src="${j.avatar}" onerror='this.onerror=null;this.src="${url_for(theme.error_img.flink)}"' alt="${j.name}" />
                    </div>
                    <div class="flink-item-name">${j.name}</div>
                    <div class="flink-item-desc" title="${j.descr}">${j.descr}</div>
                  </a>
                </div>`
            -

          - result += `${className}${classDesc} <div class="flink-list">${listResult}</div>`

        - pageContent = result + pageContent
    != pageContent

```

### 文件路径: `themes\butterfly\layout\includes\page\shuoshuo.pug`
```pug
//- - author:
//-   avatar:
//-   date:
//-   content:
//-   tags:
//-     - tag1
//-     - tag2

- page.toc = false

#article-container
  if page.comments !== false && theme.comments.use
    - commentsJsLoad = true

    script.
      (() => {
        const commentDiv = `!{partial('includes/third-party/comments/index', {}, {cache: true})}`

        const runDestroy = (shuoshuoComment) => {
          if (!shuoshuoComment) return

          for (const [key, fn] of Object.entries(shuoshuoComment)) {
            if (key.startsWith('destroy')) fn()
          }
        }

        window.addCommentToShuoshuo = e => {
          const btn = e.target.closest('.shuoshuo-comment-btn')
          if (!btn) return

          const ele = btn.closest('.container').nextElementSibling
          const { shuoshuoComment } = window
          const isInclude = ele.classList.contains('no-comment')
          runDestroy(shuoshuoComment)
          if (isInclude) {
            ele.classList.remove('no-comment')
            ele.innerHTML = commentDiv
            const key = `${location.pathname.replace(/\/$/, '')}?key=${ele.getAttribute('data-key')}`
            btf.switchComments(ele, key)
            shuoshuoComment.loadComment && shuoshuoComment.loadComment(ele, key)
          }
        }
      })()

  if page.shuoshuo_url
    script.
      (() => {
        const limitConfig = !{ JSON.stringify(page.limit || {}) }

        const sortDataByDate = data => data.sort((a, b) => new Date(b.date) - new Date(a.date))

        const filterDataByLimit = (data, limit) => {
          if (!limit || !limit.type) return data
          if (limit.type === 'num') return data.slice(0, limit.value)
          if (limit.type === 'date') {
            const limitDate = new Date(limit.value)
            return data.filter(item => new Date(item.date) >= limitDate)
          }
          return data
        };

        const formatToTimeZone = (date) => {
          const fullDate = date.length === 10 ? `${date} 00:00:00` : date
          const visitorTimeZone = '#{config.timezone}' || Intl.DateTimeFormat().resolvedOptions().timeZone
          const options = {
            timeZone: visitorTimeZone,
            year: 'numeric',
            month: '2-digit',
            day: '2-digit',
            hour: '2-digit',
            minute: '2-digit',
            second: '2-digit',
            hour12: false
          }
          const [day, month, year, hour, minute, second] = new Intl.DateTimeFormat('en-GB', options)
            .format(new Date(fullDate))
            .match(/\d+/g)
          return `${year}-${month}-${day} ${hour}:${minute}:${second}`
        }

        const loadShuoshuo = async () => {
          try {
            const response = await fetch('!{url_for(page.shuoshuo_url)}')
            let data = await response.json()

            data = filterDataByLimit(sortDataByDate(data), limitConfig)

            const container = document.getElementById('article-container')
            let start = 0

            const renderData = (dataSlice) => {
              const content = dataSlice.map(item => {
                const formattedDate = formatToTimeZone(item.date)
                const tags = item.tags && item.tags.map(tag => `<span class="shuoshuo-tag">${tag}</span>`).join('') || ''
                const commentButton = item.key && !{commentsJsLoad}
                  ? `<div class="shuoshuo-comment-btn" onclick="addCommentToShuoshuo(event)">
                      <i class="fa-solid fa-comments"></i>
                    </div>`
                  : ''
                const commentContainer = item.key
                  ? `<div class="shuoshuo-comment no-comment" data-key="${item.key}"></div>`
                  : ''

                return `
                  <div class="shuoshuo-item">
                    <div class="container">
                      <div class="shuoshuo-item-header">
                        <div class="shuoshuo-avatar">
                          <img class="no-lightbox" src="${item.avatar || '!{url_for(theme.avatar.img)}'}">
                        </div>
                        <div class="shuoshuo-info">
                          <div class="shuoshuo-author">${item.author || '!{config.author}'}</div>
                          <time class="shuoshuo-date" title="${formattedDate}">
                            ${btf.diffDate(formattedDate, true)}
                          </time>
                        </div>
                      </div>
                      <div class="shuoshuo-content">${item.content}</div>
                      <div class="shuoshuo-footer ${tags ? 'flex-between' : 'flex-end'}">
                        ${tags ? `<div class="shuoshuo-tags">${tags}</div>` : ''}
                        ${commentButton}
                      </div>
                    </div>
                    ${commentContainer}
                  </div>`
              }).join('')

              container.insertAdjacentHTML('beforeend', content)

              window.lazyLoadInstance.update()
              btf.loadLightbox(document.querySelectorAll('#article-container img:not(.no-lightbox)'))
            }

            const handleIntersection = (entries) => {
              if (!entries[0].isIntersecting) return
              observer.unobserve(entries[0].target)

              const slice = data.slice(start, start + 10)
              renderData(slice)
              start += 10

              if (start < data.length) {
                setTimeout(() => observer.observe(container.lastElementChild), 100)
              } else {
                observer.disconnect()
              }
            };

            const observer = new IntersectionObserver(handleIntersection, {
              root: null,
              rootMargin: '0px',
              threshold: 1.0
            })

            renderData(data.slice(start, 10))
            start += 10

            if (container.lastElementChild) observer.observe(container.lastElementChild)
          } catch (error) {
            console.error(error)
          }
        };

        window.pjax ? loadShuoshuo() : window.addEventListener('load', loadShuoshuo)
      })()
  else
    if site.data.shuoshuo
      each i in shuoshuoFN(site.data.shuoshuo, page)
        .shuoshuo-item
          .container
            .shuoshuo-item-header
              .shuoshuo-avatar
                img.no-lightbox(src=i.avatar || url_for(theme.avatar.img))
              .shuoshuo-info
                .shuoshuo-author=i.author || config.author
                time.shuoshuo-date(title=i.date)=i.date
            .shuoshuo-content
              !=markdown(i.content)
            .shuoshuo-footer(class=i.tags && i.tags.length ? 'flex-between' : 'flex-end')
              if i.tags
                .shuoshuo-tags
                  each tag in i.tags
                    span.shuoshuo-tag=tag
              if i.key && commentsJsLoad
                .shuoshuo-comment-btn(onclick='addCommentToShuoshuo(event)')
                  i.fa-solid.fa-comments
          if i.key && commentsJsLoad
            .shuoshuo-comment.no-comment(data-key=i.key)
```

### 文件路径: `themes\butterfly\layout\includes\page\tags.pug`
```pug
.tag-cloud-list.text-center
  !=cloudTags({source: site.tags, orderby: page.orderby || 'random', order: page.order || 1, minfontsize: 1.2, maxfontsize: 1.5, limit: 0, unit: 'em'})
```

### 文件路径: `themes\butterfly\layout\includes\post\outdate-notice.pug`
```pug
- const { limit_day, message_prev, message_next, position} = theme.noticeOutdate
- const notice_data = { limitDay: limit_day, messagePrev: message_prev, messageNext: message_next, postUpdate: full_date(page.updated)}
if position === 'top'
  #post-outdate-notice(data=notice_data hidden)
  !=page.content
else
  !=page.content
  #post-outdate-notice(data=notice_data hidden)
```

### 文件路径: `themes\butterfly\layout\includes\post\post-copyright.pug`
```pug
if theme.post_copyright.enable && page.copyright !== false
  - const author = page.copyright_author || config.author
  - const authorHref = page.copyright_author_href || theme.post_copyright.author_href || config.url
  - const url = page.copyright_url || page.permalink
  - const info = page.copyright_info || _p('post.copyright.copyright_content', theme.post_copyright.license_url, theme.post_copyright.license, config.url, config.title)
  .post-copyright
    .post-copyright__author
      span.post-copyright-meta
        i.fas.fa-circle-user.fa-fw
        = _p('post.copyright.author') + ": "
      span.post-copyright-info
        a(href=authorHref)= author
    .post-copyright__type
      span.post-copyright-meta
        i.fas.fa-square-arrow-up-right.fa-fw
        = _p('post.copyright.link') + ": "
      span.post-copyright-info
        a(href=url_for(url))= theme.post_copyright.decode ? decodeURI(url) : url
    .post-copyright__notice
      span.post-copyright-meta
        i.fas.fa-circle-exclamation.fa-fw
        = _p('post.copyright.copyright_notice') + ": "
      span.post-copyright-info!= info
```

### 文件路径: `themes\butterfly\layout\includes\post\reward.pug`
```pug
.post-reward
  .reward-button
    i.fas.fa-qrcode
    = theme.reward.text || _p('donate')
  .reward-main
    ul.reward-all
      each item in theme.reward.QR_code
        - const clickTo = item.link || item.img
        li.reward-item
          a(href=url_for(clickTo) target='_blank')
            img.post-qr-code-img(src=url_for(item.img) alt=item.text)
          .post-qr-code-desc=item.text
```

### 文件路径: `themes\butterfly\layout\includes\third-party\aplayer.pug`
```pug
link(rel='stylesheet' href=url_for(theme.asset.aplayer_css) media="print" onload="this.media='all'")
script(src=url_for(theme.asset.aplayer_js))
script(src=url_for(theme.asset.meting_js))
if theme.pjax.enable
  script.
    (() => {
      const destroyAplayer = () => {
        if (window.aplayers) {
          for (let i = 0; i < window.aplayers.length; i++) {
            if (!window.aplayers[i].options.fixed) {
              window.aplayers[i].destroy()
            }
          }
        }
      }

      const runMetingJS = () => {
        typeof loadMeting === 'function' && document.getElementsByClassName('aplayer').length && loadMeting()
      }

      btf.addGlobalFn('pjaxSend', destroyAplayer, 'destroyAplayer')
      btf.addGlobalFn('pjaxComplete', loadMeting, 'runMetingJS')
    })()

```

### 文件路径: `themes\butterfly\layout\includes\third-party\effect.pug`
```pug
if theme.fireworks && theme.fireworks.enable
  canvas.fireworks(mobile=`${theme.fireworks.mobile}`)
  script(src=url_for(theme.asset.fireworks))

if (theme.canvas_ribbon && theme.canvas_ribbon.enable)
  script(defer id="ribbon" src=url_for(theme.asset.canvas_ribbon) size=theme.canvas_ribbon.size
  alpha=theme.canvas_ribbon.alpha zIndex=theme.canvas_ribbon.zIndex mobile=`${theme.canvas_ribbon.mobile}` data-click=`${theme.canvas_ribbon.click_to_change}`)

if (theme.canvas_fluttering_ribbon && theme.canvas_fluttering_ribbon.enable)
  script(defer id="fluttering_ribbon" mobile=`${theme.canvas_fluttering_ribbon.mobile}` src=url_for(theme.asset.canvas_fluttering_ribbon))

if (theme.canvas_nest && theme.canvas_nest.enable)
  script#canvas_nest(defer color=theme.canvas_nest.color opacity=theme.canvas_nest.opacity zIndex=theme.canvas_nest.zIndex count=theme.canvas_nest.count mobile=`${theme.canvas_nest.mobile}` src=url_for(theme.asset.canvas_nest))

if theme.activate_power_mode.enable
  script(src=url_for(theme.asset.activate_power_mode))
  script.
    POWERMODE.colorful = !{theme.activate_power_mode.colorful};
    POWERMODE.shake = !{theme.activate_power_mode.shake};
    POWERMODE.mobile = !{theme.activate_power_mode.mobile};
    document.body.addEventListener('input', POWERMODE);

//- 鼠標特效
if theme.click_heart && theme.click_heart.enable
  script#click-heart(src=url_for(theme.asset.click_heart) async mobile=`${theme.click_heart.mobile}`)

if theme.clickShowText && theme.clickShowText.enable
  script#click-show-text(
    src= url_for(theme.asset.clickShowText)
    data-mobile= `${theme.clickShowText.mobile}`
    data-text= theme.clickShowText.text.join(",")
    data-fontsize= theme.clickShowText.fontSize
    data-random= `${theme.clickShowText.random}`
    async
  )
```

### 文件路径: `themes\butterfly\layout\includes\third-party\pjax.pug`
```pug
- var pjaxExclude = 'a:not([target="_blank"])'
if theme.pjax.exclude
  each val in theme.pjax.exclude
    - pjaxExclude += `:not([href="${val}"])`

- let pjaxSelectors = ['head > title', '#config-diff', '#body-wrap', '#rightside-config-hide', '#rightside-config-show', '.js-pjax']

- let choose = theme.comments.use
if choose
  if choose.includes('Livere') || choose.includes('Utterances') || choose.includes('Giscus')
    - pjaxSelectors.unshift('link[rel="canonical"]')
    if theme.Open_Graph_meta.enable
      - pjaxSelectors.unshift('meta[property="og:image"]', 'meta[property="og:title"]', 'meta[property="og:url"]', 'meta[property="og:description"]')
    else
      - pjaxSelectors.unshift('meta[name="description"]')

script(src=url_for(theme.asset.pjax))
script.
  (() => {
    const pjaxSelectors = !{JSON.stringify(pjaxSelectors)}

    window.pjax = new Pjax({
      elements: '!{pjaxExclude}',
      selectors: pjaxSelectors,
      cacheBust: false,
      analytics: !{theme.google_analytics ? true : false},
      scrollRestoration: false
    })

    const triggerPjaxFn = (val) => {
      if (!val) return
      Object.values(val).forEach(fn => fn())
    }

    document.addEventListener('pjax:send', () => {
      // removeEventListener
      btf.removeGlobalFnEvent('pjaxSendOnce')
      btf.removeGlobalFnEvent('themeChange')

      // reset readmode
      const $bodyClassList = document.body.classList
      if ($bodyClassList.contains('read-mode')) $bodyClassList.remove('read-mode')

      triggerPjaxFn(window.globalFn.pjaxSend)
    })

    document.addEventListener('pjax:complete', () => {
      btf.removeGlobalFnEvent('pjaxCompleteOnce')
      document.querySelectorAll('script[data-pjax]').forEach(item => {
        const newScript = document.createElement('script')
        const content = item.text || item.textContent || item.innerHTML || ""
        Array.from(item.attributes).forEach(attr => newScript.setAttribute(attr.name, attr.value))
        newScript.appendChild(document.createTextNode(content))
        item.parentNode.replaceChild(newScript, item)
      })

      triggerPjaxFn(window.globalFn.pjaxComplete)
    })

    document.addEventListener('pjax:error', e => {
      if (e.request.status === 404) {
        window.location.href = e.request.responseURL
      }
    })
  })()
```

### 文件路径: `themes\butterfly\layout\includes\third-party\prismjs.pug`
```pug
- const { prismjs_js, prismjs_autoloader, prismjs_lineNumber_js } = theme.asset
- const { prismjs, syntax_highlighter } = config
- const { enable, preprocess, line_number } = prismjs

if (syntax_highlighter === 'prismjs' || enable) && !preprocess
  script.
    (() => {
      window.Prism = window.Prism || {}
      window.Prism.manual = true

      const highlightAll = () => {
        window.Prism.highlightAll()
      }

      window.addEventListener('load', highlightAll)
      btf.addGlobalFn('pjaxComplete', highlightAll, 'prismjs')
      btf.addGlobalFn('encrypt', highlightAll, 'prismjs')
    })()

  script(src=url_for(prismjs_js))
  script(src=url_for(prismjs_autoloader))
  if (line_number)
    script(src=url_for(prismjs_lineNumber_js))
```

### 文件路径: `themes\butterfly\layout\includes\third-party\subtitle.pug`
```pug
- const { effect,source,sub,typed_option } = theme.subtitle
- let subContent = sub || new Array()

script.
  window.typedJSFn = {
    init: str => {
      window.typed = new Typed('#subtitle', Object.assign({
        strings: str,
        startDelay: 300,
        typeSpeed: 150,
        loop: true,
        backSpeed: 50,
      }, !{JSON.stringify(typed_option)}))
    },
    run: subtitleType => {
      if (!{effect}) {
        if (typeof Typed === 'function') {
          subtitleType()
        } else {
          btf.getScript('!{url_for(theme.asset.typed)}').then(subtitleType)
        }
      } else {
        subtitleType()
      }
    }
  }
  btf.addGlobalFn('pjaxSendOnce', () => { typed.destroy() }, 'typedDestroy')

case source
  when 1
    script.
      function subtitleType () {
        fetch('https://v1.hitokoto.cn')
          .then(response => response.json())
          .then(data => {
            if (!{effect}) {
              const from = '出自 ' + data.from
              const sub = !{JSON.stringify(subContent)}
              sub.unshift(data.hitokoto, from)
              typedJSFn.init(sub)
            } else {
              document.getElementById('subtitle').textContent = data.hitokoto
            }
          })
      }
      typedJSFn.run(subtitleType)

  when 2
    script.
      function subtitleType () {
        btf.getScript('https://yijuzhan.com/api/word.php?m=js').then(() => {
          const con = str[0]
          if (!{effect}) {
            const from = '出自 ' + str[1]
            const sub = !{JSON.stringify(subContent)}
            sub.unshift(con, from)
            typedJSFn.init(sub)
          } else {
            document.getElementById('subtitle').textContent = con
          }
        })
      }
      typedJSFn.run(subtitleType)

  when 3
    script.
      function subtitleType () {
        btf.getScript('https://sdk.jinrishici.com/v2/browser/jinrishici.js').then(() => {
          jinrishici.load(result =>{
            if (!{effect}) {
              const sub = !{JSON.stringify(subContent)}
              const content = result.data.content
              sub.unshift(content)
              typedJSFn.init(sub)
            } else {
              document.getElementById('subtitle').textContent = result.data.content
            }
          })
        })
      }
      typedJSFn.run(subtitleType)

  default
    - subContent = subContent.length ? subContent : new Array(config.subtitle)
    script.
      function subtitleType () {
        if (!{effect}) {
          typedJSFn.init(!{JSON.stringify(subContent)})
        } else {
          document.getElementById("subtitle").textContent = !{JSON.stringify(subContent[0])}
        }
      }
      typedJSFn.run(subtitleType)
```

### 文件路径: `themes\butterfly\layout\includes\third-party\umami_analytics.pug`
```pug
- let { serverURL, website_id, option, UV_PV } = theme.umami_analytics
- const isServerURL = !!serverURL
- const baseURL = serverURL ? serverURL.replace(/\/$/, '') : 'https://cloud.umami.is'
- const apiUrl = serverURL ? serverURL.replace(/\/$/, '') + '/api' : 'https://api.umami.is/v1'

script.
  (() => {
    const option = !{JSON.stringify(option)}
    const config = !{JSON.stringify(UV_PV)}

    const runTrack = () => {
      umami.track(props => ({ ...props, url: window.location.pathname, title: GLOBAL_CONFIG_SITE.title }))
    }

    const loadUmamiJS = () => {
      btf.getScript('!{baseURL}/script.js', {
        'data-website-id': '!{website_id}',
        'data-auto-track': 'false',
        ...option
      }).then(runTrack)
    }

    const getData = async (isPost) => {
      const now = Date.now()
      const keyUrl = isPost ? `&url=${window.location.pathname}` : ''
      const headerList = { 'Accept': 'application/json' }
      if (!{isServerURL}) headerList['Authorization'] = `Bearer ${config.token}`
      else headerList['x-umami-api-key'] = config.token
      const res = await fetch(`!{apiUrl}/websites/!{website_id}/stats?startAt=0000000000&endAt=${now}${keyUrl}`, {
        method: "GET",
        headers: headerList
      })
      return await res.json()
    }

    const insertData = async () => {
      try {
        if (GLOBAL_CONFIG_SITE.pageType === 'post' && config.page_pv) {
          const pagePV = document.getElementById('umamiPV')
          if (pagePV) {
            const data = await getData(true)
            pagePV.textContent = data.pageviews.value
          }
        } else {
          const data = (config.site_uv || config.site_pv) && await getData()
          if (config.site_uv) {
            const siteUV = document.getElementById('umami-site-uv')
            if (siteUV) siteUV.textContent = data.visitors.value
          }
          if (config.site_pv) {
            const sitePV = document.getElementById('umami-site-pv')
            if (sitePV) sitePV.textContent = data.pageviews.value
          }
        }
      } catch (e) {
        console.error('Failed to load Umami Analytics:', e)
      }
    }

    btf.addGlobalFn('pjaxComplete', runTrack, 'umami_analytics_run_track')
    btf.addGlobalFn('pjaxComplete', insertData, 'umami_analytics_insert')

    loadUmamiJS()
    insertData()
  })()
```

### 文件路径: `themes\butterfly\layout\includes\third-party\abcjs\abcjs.pug`
```pug
script.
  (() => {
    const abcjsInit = () => {
      const abcjsFn = () => setTimeout(() => {
        document.querySelectorAll(".abc-music-sheet").forEach(ele => {
          if (ele.children.length > 0) return
          ABCJS.renderAbc(ele, ele.innerHTML, {responsive: 'resize'})
        })
      }, 100)
      
      typeof ABCJS === 'object' ? abcjsFn()
        : btf.getScript('!{url_for(theme.asset.abcjs_basic_js)}').then(abcjsFn)
    }

    window.pjax ? abcjsInit() : window.addEventListener('load', abcjsInit)
    btf.addGlobalFn('encrypt', abcjsInit, 'abcjs')
  })()
```

### 文件路径: `themes\butterfly\layout\includes\third-party\abcjs\index.pug`
```pug
if theme.abcjs.enable
  if theme.abcjs.per_page && (['post','page'].includes(globalPageType)) || page.abcjs
    include ./abcjs.pug

```

### 文件路径: `themes\butterfly\layout\includes\third-party\card-post-count\artalk.pug`
```pug
- const { server, site } = theme.artalk

script.
  (() => {
    const getArtalkCount = async() => {
      try {
        const eleGroup = document.querySelectorAll('#recent-posts .artalk-count')
        const keyArray = Array.from(eleGroup).map(i => i.getAttribute('data-page-key'))

        const headerList = {
          method: 'GET',
        }

        const searchParams = new URLSearchParams({
          'site_name': '!{site}',
          'page_keys': keyArray
        })

        const res = await fetch(`!{server}/api/v2/stats/page_comment?${searchParams}`, headerList)
        const result = await res.json()

        keyArray.forEach((key, index) => {
          eleGroup[index].textContent = result.data[key] || 0
        })
      } catch (err) {
        console.error(err)
      }
    }

    window.pjax ? getArtalkCount() : window.addEventListener('load', getArtalkCount)
  })()
```

### 文件路径: `themes\butterfly\layout\includes\third-party\card-post-count\disqus.pug`
```pug
- const { shortname, apikey } = theme.disqus
script.
  (() => {
    const getCount = async () => {
      try {
        const eleGroup = document.querySelectorAll('#recent-posts .disqus-count')
        const cleanedLinks = Array.from(eleGroup).map(i => `thread:link=${i.href.replace(/#post-comment$/, '')}`);

        const res = await fetch(`https://disqus.com/api/3.0/threads/set.json?forum=!{shortname}&api_key=!{apikey}&${cleanedLinks.join('&')}`,{
          method: 'GET'
        })
        const result = await res.json()

        eleGroup.forEach(i => {
          const cleanedLink = i.href.replace(/#post-comment$/, '')
          const urlData = result.response.find(data => data.link === cleanedLink) || { posts: 0 }
          i.textContent = urlData.posts
        })
      } catch (err) {
        console.error(err)
      }
    }

    window.pjax ? getCount() : window.addEventListener('load', getCount)
  })()

```

### 文件路径: `themes\butterfly\layout\includes\third-party\card-post-count\fb.pug`
```pug
- const fbSDKVer = 'v20.0'
- const fbSDK = `https://connect.facebook.net/${theme.facebook_comments.lang}/sdk.js#xfbml=1&version=${fbSDKVer}`

script.
  (()=>{
    function loadFBComment () {
      if (typeof FB === 'object') FB.XFBML.parse(document.getElementById('recent-posts'))
      else {
        let ele = document.createElement('script')
        ele.setAttribute('src','!{fbSDK}')
        ele.setAttribute('async', 'true')
        ele.setAttribute('defer', 'true')
        ele.setAttribute('crossorigin', 'anonymous')
        document.body.appendChild(ele)
      }
    }
    window.pjax ? loadFBComment() : window.addEventListener('load', loadFBComment)
  })()

```

### 文件路径: `themes\butterfly\layout\includes\third-party\card-post-count\index.pug`
```pug
case theme.comments.use[0]
  when 'Twikoo'
    include ./twikoo.pug
  when 'Disqus'
  when 'Disqusjs'
    include ./disqus.pug
  when 'Valine'
    include ./valine.pug
  when 'Waline'
    include ./waline.pug
  when 'Facebook Comments'
    include ./fb.pug
  when 'Remark42'
    include ./remark42.pug
  when 'Artalk'
    include ./artalk.pug
```

### 文件路径: `themes\butterfly\layout\includes\third-party\card-post-count\remark42.pug`
```pug
- const { host, siteId, option } = theme.remark42

script.
  (()=>{
    window.remark_config = Object.assign({
      host: '!{host}',
      site_id: '!{siteId}',
    },!{JSON.stringify(option)})

    function getCount () {
      const s = document.createElement('script')
      s.src = remark_config.host + '/web/counter.js'
      s.defer = true
      document.head.appendChild(s)
    }

    window.pjax ? getCount() : window.addEventListener('load', getCount)
  })()
```

### 文件路径: `themes\butterfly\layout\includes\third-party\card-post-count\twikoo.pug`
```pug
script.
  (() => { 
    const getCommentUrl = () => {
      const eleGroup = document.querySelectorAll('#recent-posts .article-title')
      let urlArray = []
      eleGroup.forEach(i=>{
        urlArray.push(i.getAttribute('href'))
      })
      return urlArray
    }

    const getCount = () => {
      const runTwikoo = () => {
        twikoo.getCommentsCount({
          envId: '!{theme.twikoo.envId}',
          region: '!{theme.twikoo.region}',
          urls: getCommentUrl(),
          includeReply: false
        }).then(function (res) {
          document.querySelectorAll('#recent-posts .twikoo-count').forEach((item,index) => {
            item.textContent = res[index].count
          })
        }).catch(function (err) {
          console.log(err)
        })
      }

        if (typeof twikoo === 'object') {
          runTwikoo()
        } else {
          btf.getScript('!{url_for(theme.asset.twikoo)}').then(runTwikoo)
        }
    }

    window.pjax ? getCount() : window.addEventListener('load', getCount)

  })()
```

### 文件路径: `themes\butterfly\layout\includes\third-party\card-post-count\valine.pug`
```pug
script.
  (() => {
    function loadValine () {
      function initValine () {
        let initData = {
          el: '#vcomment',
          appId: '#{theme.valine.appId}',
          appKey: '#{theme.valine.appKey}',
          serverURLs: '#{theme.valine.serverURLs}'
        }
        
        const valine = new Valine(initData)
      }

      if (typeof Valine === 'function') initValine() 
      else btf.getScript('!{url_for(theme.asset.valine)}').then(initValine)
    }

    window.pjax ? loadValine() : window.addEventListener('load', loadValine)
  })()

```

### 文件路径: `themes\butterfly\layout\includes\third-party\card-post-count\waline.pug`
```pug
- const serverURL = theme.waline.serverURL.replace(/\/$/, '')
script.
  (() => {
    async function loadWaline () {
      try {
        const eleGroup = document.querySelectorAll('#recent-posts .waline-comment-count')
        const keyArray = Array.from(eleGroup).map(i => i.getAttribute('data-path'))

        const res = await fetch(`!{serverURL}/api/comment?type=count&url=${keyArray}`, { method: 'GET' })
        const result = await res.json()
        
        result.data.forEach((count, index) => {
          eleGroup[index].textContent = count
        })
      } catch (err) {
        console.error(err)
      }
    }

    window.pjax ? loadWaline() : window.addEventListener('load', loadWaline)
  })()

```

### 文件路径: `themes\butterfly\layout\includes\third-party\chat\chatra.pug`
```pug
//- https://chatra.io/help/api/
script.
  (() => {
    window.ChatraID = '#{theme.chatra.id}'
    window.Chatra = window.Chatra || function() {
      (window.Chatra.q = window.Chatra.q || []).push(arguments)
    }

    btf.getScript('https://call.chatra.io/chatra.js').then(() => {
      const isChatBtn = !{theme.chat.rightside_button}
      const isChatHideShow = !{theme.chat.button_hide_show}

      if (isChatBtn) {
        const close = () => {
          Chatra('minimizeWidget')
          Chatra('hide')
        }

        const open = () => {
          Chatra('openChat', true)
          Chatra('show')
        }

        window.ChatraSetup = { startHidden: true }
      
        window.chatBtnFn = () => document.getElementById('chatra').classList.contains('chatra--expanded') ? close() : open()

        document.getElementById('chat-btn').style.display = 'block'
      } else if (isChatHideShow) {
        window.chatBtn = {
          hide: () => Chatra('hide'),
          show: () => Chatra('show')
        }
      }
    })
  })()



```

### 文件路径: `themes\butterfly\layout\includes\third-party\chat\crisp.pug`
```pug
script.
  (() => {
    window.$crisp = ['safe', true]
    window.CRISP_WEBSITE_ID = "!{theme.crisp.website_id}"

    btf.getScript('https://client.crisp.chat/l.js').then(() => {
      const isChatBtn = !{theme.chat.rightside_button}
      const isChatHideShow = !{theme.chat.button_hide_show}

      if (isChatBtn) {
        const open = () => {
          $crisp.push(["do", "chat:show"])
          $crisp.push(["do", "chat:open"])
        }

        const close = () => $crisp.push(["do", "chat:hide"])

        close()

        $crisp.push(["on", "chat:closed", close])

        window.chatBtnFn = () => $crisp.is("chat:visible") ? close() : open()

        document.getElementById('chat-btn').style.display = 'block'
      } else if (isChatHideShow) {
        window.chatBtn = {
          hide: () => $crisp.push(["do", "chat:hide"]),
          show: () => $crisp.push(["do", "chat:show"])
        }
      }
    })
  })()
```

### 文件路径: `themes\butterfly\layout\includes\third-party\chat\index.pug`
```pug
case theme.chat.use
  when 'chatra'
    include ./chatra.pug
  when 'tidio'
    include ./tidio.pug
  when 'crisp'
    include ./crisp.pug
```

### 文件路径: `themes\butterfly\layout\includes\third-party\chat\tidio.pug`
```pug
script.
  (() => {
    btf.getScript('//code.tidio.co/!{theme.tidio.public_key}.js').then(() => {
      const isChatBtn = !{theme.chat.rightside_button}
      const isChatHideShow = !{theme.chat.button_hide_show}

      if (isChatBtn) {
        let isShow = false
        const close = () => {
          window.tidioChatApi.hide()
          isShow = false
        }
        
        const open = () => {
          window.tidioChatApi.open()
          window.tidioChatApi.show()
          isShow = true
        }

        const onTidioChatApiReady = () => {
          window.tidioChatApi.hide()
          window.tidioChatApi.on("close", close)
        }
        if (window.tidioChatApi) {
          window.tidioChatApi.on("ready", onTidioChatApiReady)
        } else {
          document.addEventListener("tidioChat-ready", onTidioChatApiReady)
        }

        window.chatBtnFn = () => {
          if (!window.tidioChatApi) return
          isShow ? close() : open()
        }

        document.getElementById('chat-btn').style.display = 'block'

      } else if (isChatHideShow) {
        window.chatBtn = {
          hide: () => window.tidioChatApi && window.tidioChatApi.hide(),
          show: () => window.tidioChatApi && window.tidioChatApi.show()
        }
      }
    })
  })()


```

### 文件路径: `themes\butterfly\layout\includes\third-party\comments\artalk.pug`
```pug
- const { server, site, option } = theme.artalk
- const { use, lazyload } = theme.comments

script.
  (() => {
    let artalkItem = null
    const option = !{JSON.stringify(option)}
    const isShuoshuo = GLOBAL_CONFIG_SITE.pageType === 'shuoshuo'

    const destroyArtalk = () => {
      if (artalkItem) {
        artalkItem.destroy()
        artalkItem = null
      }
    }

    const artalkChangeMode = theme => artalkItem && artalkItem.setDarkMode(theme === 'dark')

    const initArtalk = (el = document, pageKey = location.pathname) => {
      artalkItem = Artalk.init({
        el: el.querySelector('#artalk-wrap'),
        server: '!{server}',
        site: '!{site}',
        darkMode: document.documentElement.getAttribute('data-theme') === 'dark',
        ...option,
        pageKey: isShuoshuo ? pageKey : (option && option.pageKey) || pageKey
      })

      if (GLOBAL_CONFIG.lightbox === 'null') return
      artalkItem.on('list-loaded', () => {
        artalkItem.ctx.get('list').getCommentNodes().forEach(comment => {
          const $content = comment.getRender().$content
          btf.loadLightbox($content.querySelectorAll('img:not([atk-emoticon])'))
        })
      })

      if (isShuoshuo) {
        window.shuoshuoComment.destroyArtalk = () => {
          destroyArtalk()
          if (el.children.length) {
            el.innerHTML = ''
            el.classList.add('no-comment')
          }
        }
      }

      btf.addGlobalFn('pjaxSendOnce', destroyArtalk, 'destroyArtalk')
      btf.addGlobalFn('themeChange', artalkChangeMode, 'artalk')
    }

    const loadArtalk = async (el, pageKey) => {
      if (typeof Artalk === 'object') initArtalk(el, pageKey)
      else {
        await btf.getCSS('!{theme.asset.artalk_css}')
        await btf.getScript('!{theme.asset.artalk_js}')
        initArtalk(el, pageKey)
      }
    }

    if (isShuoshuo) {
      '!{use[0]}' === 'Artalk'
        ? window.shuoshuoComment = { loadComment: loadArtalk }
        : window.loadOtherComment = loadArtalk
      return
    }

    if ('!{use[0]}' === 'Artalk' || !!{lazyload}) {
      if (!{lazyload}) btf.loadComment(document.getElementById('artalk-wrap'), loadArtalk)
      else setTimeout(loadArtalk, 100)
    } else {
      window.loadOtherComment = loadArtalk
    }
  })()
```

### 文件路径: `themes\butterfly\layout\includes\third-party\comments\disqus.pug`
```pug
- const disqusPageTitle = page.title.replace(/'/ig,"\\'")
- const { shortname, apikey } = theme.disqus
- const { use, lazyload, count } = theme.comments

script.
  (() => {
    const isShuoshuo = GLOBAL_CONFIG_SITE.pageType === 'shuoshuo'

    const disqusReset = conf => {
      window.DISQUS && window.DISQUS.reset({
        reload: true,
        config: conf
      })
    }

    const loadDisqus = (el, path) => {
      if (isShuoshuo) {
        window.shuoshuoComment.destroyDisqus = () => {
          if (el.children.length) {
            el.innerHTML = ''
            el.classList.add('no-comment')
          }
        }
      }

      window.disqus_identifier = isShuoshuo ? path : '!{ url_for(page.path) }'
      window.disqus_url = isShuoshuo ? location.origin + path : '!{ page.permalink }'

      const disqus_config = function () {
        this.page.url = disqus_url
        this.page.identifier = disqus_identifier
        this.page.title = '!{ disqusPageTitle }'
      }

      if (window.DISQUS) disqusReset(disqus_config)
      else {
        const script = document.createElement('script')
        script.src = 'https://!{shortname}.disqus.com/embed.js'
        script.setAttribute('data-timestamp', +new Date())
        document.head.appendChild(script)
      }

      btf.addGlobalFn('themeChange', () => disqusReset(disqus_config), 'disqus')
    }

    const getCount = async() => {
      try {
        const eleGroup = document.querySelector('#post-meta .disqus-comment-count')
        if (!eleGroup) return
        const cleanedLinks = eleGroup.href.replace(/#post-comment$/, '')

        const res = await fetch(`https://disqus.com/api/3.0/threads/set.json?forum=!{shortname}&api_key=!{apikey}&thread:link=${cleanedLinks}`,{
          method: 'GET'
        })
        const result = await res.json()

        const count = result.response.length ? result.response[0].posts : 0
        eleGroup.textContent = count
      } catch (err) {
        console.error(err)
      }
    }

    if (isShuoshuo) {
      '!{use[0]}' === 'Disqus'
        ? window.shuoshuoComment = { loadComment: loadDisqus }
        : window.loadOtherComment = loadDisqus
      return
    }

    if ('!{use[0]}' === 'Disqus' || !!{lazyload}) {
      if (!{lazyload}) btf.loadComment(document.getElementById('disqus_thread'), loadDisqus)
      else {
        loadDisqus()
        !{ count ? `GLOBAL_CONFIG_SITE.pageType === 'post' && getCount()` : '' }
      }
    } else {
      window.loadOtherComment = loadDisqus
    }
  })()

```

### 文件路径: `themes\butterfly\layout\includes\third-party\comments\disqusjs.pug`
```pug
- let disqusjsPageTitle = page.title && page.title.replace(/'/ig,"\\'")
- const { shortname:dqShortname, apikey:dqApikey, option:dqOption } = theme.disqusjs

script.
  (() => {
    const isShuoshuo = GLOBAL_CONFIG_SITE.pageType === 'shuoshuo'== 'shuoshuo'
    const dqOption = !{JSON.stringify(dqOption)}

    const destroyDisqusjs = () => {
      disqusjs.destroy()
      window.disqusjs = null
    }

    const themeChange = (el, path) => {
      destroyDisqusjs()
      initDisqusjs(el, path)
    }

    const initDisqusjs = (el = document, path) => {
      if (isShuoshuo) {
        window.shuoshuoComment.destroyDisqusjs = () => {
          destroyDisqusjs()
          if (el.children.length) {
            el.innerHTML = ''
            el.classList.add('no-comment')
          }
        }
      }

      disqusjs = new DisqusJS({
        shortname: '!{dqShortname}',
        title: '!{ disqusjsPageTitle }',
        apikey: '!{dqApikey}',
        ...dqOption,
        identifier: isShuoshuo ? path : (dqOption && dqOption.identifier) || '!{ url_for(page.path) }',
        url: isShuoshuo ? location.origin + path : (dqOption && dqOption.url) || '!{ page.permalink }'
      })

      disqusjs.render(el.querySelector('#disqusjs-wrap'))

      btf.addGlobalFn('themeChange', () => themeChange(el, path), 'disqusjs')
    }

    const loadDisqusjs = async(el, path) => {
      if (window.disqusJsLoad) initDisqusjs(el, path)
      else {
        await btf.getCSS('!{url_for(theme.asset.disqusjs_css)}')
        await btf.getScript('!{url_for(theme.asset.disqusjs)}')
        initDisqusjs(el, path)
        window.disqusJsLoad = true
      }
    }

    const getCount = async() => {
      try {
        const eleGroup = document.querySelector('#post-meta .disqusjs-comment-count')
        if (!eleGroup) return
        const cleanedLinks = eleGroup.href.replace(/#post-comment$/, '')

        const res = await fetch(`https://disqus.com/api/3.0/threads/set.json?forum=!{dqShortname}&api_key=!{dqApikey}&thread:link=${cleanedLinks}`,{
          method: 'GET'
        })
        const result = await res.json()
        const count = result.response.length ? result.response[0].posts : 0
        eleGroup.textContent = count
      } catch (err) {
        console.error(err)
      }
    }

    if (isShuoshuo) {
      '!{theme.comments.use[0]}' === 'Disqusjs'
        ? window.shuoshuoComment = { loadComment: loadDisqusjs }
        : window.loadOtherComment = loadDisqusjs
      return
    }

    if ('!{theme.comments.use[0]}' === 'Disqusjs' || !!{theme.comments.lazyload}) {
      if (!{theme.comments.lazyload}) btf.loadComment(document.getElementById('disqusjs-wrap'), loadDisqusjs)
      else {
        loadDisqusjs()
        !{ theme.comments.count ? `GLOBAL_CONFIG_SITE.pageType === 'post' && getCount()` : '' }
      }
    } else {
      window.loadOtherComment = loadDisqusjs
    }
  })()
```

### 文件路径: `themes\butterfly\layout\includes\third-party\comments\facebook_comments.pug`
```pug
- const fbSDKVer = 'v20.0'
- const fbSDK = `https://connect.facebook.net/${theme.facebook_comments.lang}/sdk.js#xfbml=1&version=${fbSDKVer}`

script.
  (()=>{
    const isShuoshuo = GLOBAL_CONFIG_SITE.pageType === 'shuoshuo'== 'shuoshuo'

    const loadFBComment = (el = document, path) => {
      if (isShuoshuo) {
        window.shuoshuoComment.destroyFB = () => {
          if (el.children.length) {
            el.innerHTML = ''
            el.classList.add('no-comment')
          }
        }
      }

      document.getElementById('fb-root') ? '' : document.body.insertAdjacentHTML('afterend', '<div id="fb-root"></div>')

      const themeNow = document.documentElement.getAttribute('data-theme') === 'dark' ? 'dark' : 'light'
      const $fbComment = el.getElementsByClassName('fb-comments')[0]
      $fbComment.setAttribute('data-colorscheme',themeNow)
      $fbComment.setAttribute('data-href', isShuoshuo ? '!{urlNoIndex(page.permalink)}' + '#' + path : '!{urlNoIndex(page.permalink)}')

      if (typeof FB === 'object') {
        FB.XFBML.parse(document.getElementsByClassName('post-meta-commentcount')[0])
        FB.XFBML.parse(el.querySelector('#post-comment'))
      }
      else {
        let ele = document.createElement('script')
        ele.setAttribute('src','!{fbSDK}')
        ele.setAttribute('async', 'true')
        ele.setAttribute('defer', 'true')
        ele.setAttribute('crossorigin', 'anonymous')
        ele.setAttribute('id', 'facebook-jssdk')
        document.getElementById('fb-root').insertAdjacentElement('afterbegin',ele)
      }
    }

    const fbModeChange = theme => {
      const $fbComment = document.getElementsByClassName('fb-comments')[0]
      if ($fbComment && typeof FB === 'object') {
        $fbComment.setAttribute('data-colorscheme',theme)
        FB.XFBML.parse(document.getElementById('post-comment'))
      }
    }

    btf.addGlobalFn('themeChange', fbModeChange, 'facebook_comments')

    if (isShuoshuo) {
      '!{theme.comments.use[0]}' === 'Facebook Comments'
        ? window.shuoshuoComment = { loadComment: loadFBComment }
        : window.loadOtherComment = loadFBComment
      return
    }

    if ('!{theme.comments.use[0]}' === 'Facebook Comments' || !!{theme.comments.lazyload}) {
      if (!{theme.comments.lazyload}) btf.loadComment(document.querySelector('#post-comment .fb-comments'), loadFBComment)
      else loadFBComment()
    } else {
      window.loadOtherComment = loadFBComment
    }
  })()


```

### 文件路径: `themes\butterfly\layout\includes\third-party\comments\giscus.pug`
```pug
- const { use, lazyload } = theme.comments
- const { repo, repo_id, category_id, light_theme, dark_theme, js, option } = theme.giscus
- const giscusUrl = js || 'https://giscus.app/client.js'
- const giscusOriginUrl = new URL(giscusUrl).origin

script.
  (() => {
    const isShuoshuo = GLOBAL_CONFIG_SITE.pageType === 'shuoshuo'
    const option = !{JSON.stringify(option)}

    const getGiscusTheme = theme => theme === 'dark' ? '!{dark_theme}' : '!{light_theme}'

    const createScriptElement = config => {
      const ele = document.createElement('script')
      Object.entries(config).forEach(([key, value]) => {
        ele.setAttribute(key, value)
      })
      return ele
    }

    const loadGiscus = (el = document, key) => {
      const mappingConfig = isShuoshuo
        ? { 'data-mapping': 'specific', 'data-term': key }
        : { 'data-mapping': (option && option['data-mapping']) || 'pathname' }

      const giscusConfig = {
        src: '!{giscusUrl}',
        'data-repo': '!{repo}',
        'data-repo-id': '!{repo_id}',
        'data-category-id': '!{category_id}',
        'data-theme': getGiscusTheme(document.documentElement.getAttribute('data-theme')),
        'data-reactions-enabled': '1',
        crossorigin: 'anonymous',
        async: true,
        ...option,
        ...mappingConfig
      }

      const scriptElement = createScriptElement(giscusConfig)

      el.querySelector('#giscus-wrap').appendChild(scriptElement)

      if (isShuoshuo) {
        window.shuoshuoComment.destroyGiscus = () => {
          if (el.children.length) {
            el.innerHTML = ''
            el.classList.add('no-comment')
          }
        }
      }
    }

    const changeGiscusTheme = theme => {
      const iframe = document.querySelector('#giscus-wrap iframe')
      if (iframe) {
        const message = {
          giscus: {
            setConfig: {
              theme: getGiscusTheme(theme)
            }
          }
        }
        iframe.contentWindow.postMessage(message, '!{giscusOriginUrl}')
      }
    }

    btf.addGlobalFn('themeChange', changeGiscusTheme, 'giscus')

    if (isShuoshuo) {
      '!{use[0]}' === 'Giscus'
        ? window.shuoshuoComment = { loadComment: loadGiscus }
        : window.loadOtherComment = loadGiscus
      return
    }

    if ('!{use[0]}' === 'Giscus' || !!{lazyload}) {
      if (!{lazyload}) btf.loadComment(document.getElementById('giscus-wrap'), loadGiscus)
      else loadGiscus()
    } else {
      window.loadOtherComment = loadGiscus
    }
  })()

```

### 文件路径: `themes\butterfly\layout\includes\third-party\comments\gitalk.pug`
```pug
- const { client_id, client_secret, repo, owner, admin, option } = theme.gitalk

script.
  (() => {
    const isShuoshuo = GLOBAL_CONFIG_SITE.pageType === 'shuoshuo'
    const option = !{JSON.stringify(option)}

    const commentCount = n => {
      const isCommentCount = document.querySelector('#post-meta .gitalk-comment-count')
      if (isCommentCount) {
        isCommentCount.textContent= n
      }
    }

    const initGitalk = (el, path) => {
      if (isShuoshuo) {
        window.shuoshuoComment.destroyGitalk = () => {
          if (el.children.length) {
            el.innerHTML = ''
            el.classList.add('no-comment')
          }
        }
      }

      const gitalk = new Gitalk({
        clientID: '!{client_id}',
        clientSecret: '!{client_secret}',
        repo: '!{repo}',
        owner: '!{owner}',
        admin: ['!{admin}'],
        updateCountCallback: commentCount,
        ...option,
        id: isShuoshuo ? path : (option && option.id) || '!{md5(page.path)}'
      })

      gitalk.render('gitalk-container')
    }

    const loadGitalk = async(el, path) => {
      if (typeof Gitalk === 'function') initGitalk(el, path)
      else {
        await btf.getCSS('!{url_for(theme.asset.gitalk_css)}')
        await btf.getScript('!{url_for(theme.asset.gitalk)}')
        initGitalk(el, path)
      }
    }

    if (isShuoshuo) {
      '!{theme.comments.use[0]}' === 'Gitalk'
        ? window.shuoshuoComment = { loadComment: loadGitalk }
        : window.loadOtherComment = loadGitalk
      return
    }

    if ('!{theme.comments.use[0]}' === 'Gitalk' || !!{theme.comments.lazyload}) {
      if (!{theme.comments.lazyload}) btf.loadComment(document.getElementById('gitalk-container'), loadGitalk)
      else loadGitalk()
    } else {
      window.loadOtherComment = loadGitalk
    }
  })()




```

### 文件路径: `themes\butterfly\layout\includes\third-party\comments\index.pug`
```pug
- let defaultComment = theme.comments.use[0]
hr.custom-hr
#post-comment
  .comment-head
    .comment-headline
      i.fas.fa-comments.fa-fw
      span= ' ' + _p('comment')
    
    if theme.comments.use.length > 1
      .comment-switch
        span.first-comment=defaultComment
        span#switch-btn
        span.second-comment=theme.comments.use[1]


  .comment-wrap
    each name in theme.comments.use
      div
        case name
          when 'Disqus'
            #disqus_thread
          when 'Valine'
            #vcomment.vcomment
          when 'Disqusjs'
            #disqusjs-wrap
          when 'Livere'
            #lv-container(data-id="city" data-uid=theme.livere.uid)
          when 'Gitalk'
            #gitalk-container
          when 'Utterances'
            #utterances-wrap
          when 'Twikoo'
            #twikoo-wrap
          when 'Waline'
            #waline-wrap
          when 'Giscus'
            #giscus-wrap
          when 'Facebook Comments'
            .fb-comments(data-colorscheme = theme.display_mode === 'dark' ? 'dark' : 'light'
                        data-numposts= theme.facebook_comments.pageSize || 10
                        data-order-by= theme.facebook_comments.order_by || 'social'
                        data-width="100%")
          when 'Remark42'
            #remark42
          when 'Artalk'
            #artalk-wrap

```

### 文件路径: `themes\butterfly\layout\includes\third-party\comments\js.pug`
```pug
each name in theme.comments.use
  case name
    when 'Valine'
      !=partial('includes/third-party/comments/valine', {}, {cache: true})
    when 'Disqus'
      include ./disqus.pug
    when 'Disqusjs'
      include ./disqusjs.pug
    when 'Livere'
      !=partial('includes/third-party/comments/livere', {}, {cache: true})
    when 'Gitalk'
      include ./gitalk.pug
    when 'Utterances'
      !=partial('includes/third-party/comments/utterances', {}, {cache: true})
    when 'Twikoo'
      !=partial('includes/third-party/comments/twikoo', {}, {cache: true})
    when 'Waline'
      !=partial('includes/third-party/comments/waline', {}, {cache: true})
    when 'Giscus'
      !=partial('includes/third-party/comments/giscus', {}, {cache: true})
    when 'Facebook Comments'
      include ./facebook_comments.pug
    when 'Remark42'
      !=partial('includes/third-party/comments/remark42', {}, {cache: true})
    when 'Artalk'
      !=partial('includes/third-party/comments/artalk', {}, {cache: true})
```

### 文件路径: `themes\butterfly\layout\includes\third-party\comments\livere.pug`
```pug
- const { use, lazyload } = theme.comments

script.
  (() => {
    const isShuoshuo = GLOBAL_CONFIG_SITE.pageType === 'shuoshuo'

    const loadLivere = (el, path) => {
      window.livereOptions = {
        refer: path || location.pathname
      }

      if (isShuoshuo) {
        window.shuoshuoComment.destroyLivere = () => {
          if (el.children.length) {
            el.innerHTML = ''
            el.classList.add('no-comment')
          }
        }
      }

      if (typeof LivereTower === 'object') window.LivereTower.init()
      else {
        (function(d, s) {
            var j, e = d.getElementsByTagName(s)[0];
            if (typeof LivereTower === 'function') { return; }
            j = d.createElement(s);
            j.src = 'https://cdn-city.livere.com/js/embed.dist.js';
            j.async = true;
            e.parentNode.insertBefore(j, e);
        })(document, 'script');
      }
    }

    if (isShuoshuo) {
      '!{use[0]}' === 'Livere'
        ? window.shuoshuoComment = { loadComment: loadLivere }
        : window.loadOtherComment = loadLivere
      return
    }
  
    if ('!{use[0]}' === 'Livere' || !!{lazyload}) {
      if (!{lazyload}) btf.loadComment(document.getElementById('lv-container'), loadLivere)
      else loadLivere()
    } else {
      window.loadOtherComment = loadLivere
    }
  })()
```

### 文件路径: `themes\butterfly\layout\includes\third-party\comments\remark42.pug`
```pug
- const { host, siteId, option } = theme.remark42

script.
  (() => {
    const isShuoshuo = GLOBAL_CONFIG_SITE.pageType === 'shuoshuo'
    const option = !{JSON.stringify(option)}

    const loadScript = src => {
      const script = document.createElement('script')
      script.src = src
      script.defer = true
      document.head.appendChild(script)
    }

    const addRemark42 = () => loadScript('!{host}/web/embed.js')

    const getCount = () => document.querySelector('.remark42__counter') && loadScript('!{host}/web/count.js')

    const destroyRemark42 = () => window.remark42Instance && window.remark42Instance.destroy()

    const initRemark42 = remark_config => {
      if (window.REMARK42) {
        destroyRemark42()
        window.remark42Instance = window.REMARK42.createInstance({
          ...remark_config
        })
      }
    }

    const loadRemark42 = (el, path) => {
      if (isShuoshuo) {
        window.shuoshuoComment.destroyRemark42 = () => {
          destroyRemark42()
          if (el.children.length) {
            el.innerHTML = ''
            el.classList.add('no-comment')
          }
        }
      }

      window.remark_config = {
        host: '!{host}',
        site_id: '!{siteId}',
        theme: document.documentElement.getAttribute('data-theme') === 'dark' ? 'dark' : 'light',
        ...option,
        url: isShuoshuo ? window.location.origin + path : (option && option.url) || window.location.origin + window.location.pathname
      }

      if (window.REMARK42) {
        initRemark42(remark_config)
        getCount()
      } else {
        addRemark42()
        window.addEventListener('REMARK42::ready', () => {
          initRemark42(remark_config)
          getCount()
        })
      }
    }

    const remarkChangeMode = theme => window.REMARK42 && window.REMARK42.changeTheme(theme)

    btf.addGlobalFn('themeChange', remarkChangeMode, 'remark42')

    if (isShuoshuo) {
      '!{theme.comments.use[0]}' === 'Remark42'
        ? window.shuoshuoComment = { loadComment: loadRemark42 }
        : window.loadOtherComment = loadRemark42
      return
    }
    
    if ('!{theme.comments.use[0]}' === 'Remark42' || !!{theme.comments.lazyload}) {
      if (!{theme.comments.lazyload}) btf.loadComment(document.getElementById('remark42'), loadRemark42)
      else loadRemark42()
    } else {
      window.loadOtherComment = loadRemark42
    }
  })()
```

### 文件路径: `themes\butterfly\layout\includes\third-party\comments\twikoo.pug`
```pug
- const { envId, region, option } = theme.twikoo
- const { use, lazyload, count } = theme.comments

script.
  (() => {
    const isShuoshuo = GLOBAL_CONFIG_SITE.pageType === 'shuoshuo'
    const option = !{JSON.stringify(option)}

    const getCount = () => {
      const countELement = document.getElementById('twikoo-count')
      if(!countELement) return
      twikoo.getCommentsCount({
        envId: '!{envId}',
        region: '!{region}',
        urls: [window.location.pathname],
        includeReply: false
      }).then(res => {
        countELement.textContent = res[0].count
      }).catch(err => {
        console.error(err)
      })
    }

    const init = (el = document, path = location.pathname) => {
      twikoo.init({
        el: el.querySelector('#twikoo-wrap'),
        envId: '!{envId}',
        region: '!{region}',
        onCommentLoaded: () => {
          btf.loadLightbox(document.querySelectorAll('#twikoo .tk-content img:not(.tk-owo-emotion)'))
        },
        ...option,
        path: isShuoshuo ? path : (option && option.path) || path
      })

      !{count ? `GLOBAL_CONFIG_SITE.pageType === 'post' && getCount()` : ''}

      isShuoshuo && (window.shuoshuoComment.destroyTwikoo = () => {
        if (el.children.length) {
          el.innerHTML = ''
          el.classList.add('no-comment')
        }
      })
    }

    const loadTwikoo = (el, path) => {
      if (typeof twikoo === 'object') setTimeout(() => init(el, path), 0)
      else btf.getScript('!{url_for(theme.asset.twikoo)}').then(() => init(el, path))
    }

    if (isShuoshuo) {
      '!{use[0]}' === 'Twikoo'
        ? window.shuoshuoComment = { loadComment: loadTwikoo }
        : window.loadOtherComment = loadTwikoo
      return
    }

    if ('!{use[0]}' === 'Twikoo' || !!{lazyload}) {
      if (!{lazyload}) btf.loadComment(document.getElementById('twikoo-wrap'), loadTwikoo)
      else loadTwikoo()
    } else {
      window.loadOtherComment = loadTwikoo
    }
  })()
```

### 文件路径: `themes\butterfly\layout\includes\third-party\comments\utterances.pug`
```pug
- const { use, lazyload } = theme.comments
- const { repo, issue_term, light_theme, dark_theme, js, option } = theme.utterances
- const utterancesUrl = js || 'https://utteranc.es/client.js'
- const utterancesOriginUrl = new URL(utterancesUrl).origin

script.
  (() => {
    const isShuoshuo = GLOBAL_CONFIG_SITE.pageType === 'shuoshuo'
    const option = !{JSON.stringify(option)}
    const getUtterancesTheme = theme => theme === 'dark' ? '#{dark_theme}' : '#{light_theme}'

    const loadUtterances = (el = document, key) => {
      if (isShuoshuo) {
        window.shuoshuoComment.destroyUtterances = () => {
          if (el.children.length) {
            el.innerHTML = ''
            el.classList.add('no-comment')
          }
        }
      }

      const config = {
        src: '!{utterancesUrl}',
        repo: '!{repo}',
        theme: getUtterancesTheme(document.documentElement.getAttribute('data-theme')),
        crossorigin: 'anonymous',
        async: true,
        ...option,
        'issue-term': isShuoshuo ? key : (option && option['issue-term']) || '!{issue_term}'
      }

      const ele = document.createElement('script')
      Object.entries(config).forEach(([key, value]) => ele.setAttribute(key, value))
      el.querySelector('#utterances-wrap').appendChild(ele)
    }

    const changeUtterancesTheme = theme => {
      const iframe = document.querySelector('#utterances-wrap iframe')
      if (iframe) {
        const message = {
          type: 'set-theme',
          theme: getUtterancesTheme(theme)
        };
        iframe.contentWindow.postMessage(message, '!{utterancesOriginUrl}')
      }
    }

    btf.addGlobalFn('themeChange', changeUtterancesTheme, 'utterances')

    if (isShuoshuo) {
      '!{use[0]}' === 'Utterances'
        ? window.shuoshuoComment = { loadComment: loadUtterances }
        : window.loadOtherComment = loadUtterances
      return
    }
    
    if ('!{use[0]}' === 'Utterances' || !!{lazyload}) {
      if (!{lazyload}) btf.loadComment(document.getElementById('utterances-wrap'), loadUtterances)
      else loadUtterances()
    } else {
      window.loadOtherComment = loadUtterances
    }
  })()
```

### 文件路径: `themes\butterfly\layout\includes\third-party\comments\valine.pug`
```pug
- const { use, lazyload } = theme.comments
- const { appId, appKey, avatar, serverURLs, visitor, option } = theme.valine

- let emojiMaps = '""'
if site.data.valine
  - emojiMaps = JSON.stringify(site.data.valine)

script.
  (() => {
    const isShuoshuo = GLOBAL_CONFIG_SITE.pageType === 'shuoshuo'
    const option = !{JSON.stringify(option)}

    const initValine = (el, path) => {
      if (isShuoshuo) {
        window.shuoshuoComment.destroyValine = () => {
          if (el.children.length) {
            el.innerHTML = ''
            el.classList.add('no-comment')
          }
        }
      }

      const valineConfig = {
        el: '#vcomment',
        appId: '#{appId}',
        appKey: '#{appKey}',
        avatar: '#{avatar}',
        serverURLs: '#{serverURLs}',
        emojiMaps: !{emojiMaps},
        visitor: #{visitor},
        ...option,
        path: isShuoshuo ? path : (option && option.path) || window.location.pathname
      }

      new Valine(valineConfig)
    }

    const loadValine = async (el, path) => {
      if (typeof Valine === 'function') {
        initValine(el, path)
      } else {
        await btf.getScript('!{url_for(theme.asset.valine)}')
        initValine(el, path)
      }
    }

    if (isShuoshuo) {
      '!{use[0]}' === 'Valine'
        ? window.shuoshuoComment = { loadComment: loadValine }
        : window.loadOtherComment = loadValine
      return
    }

    if ('!{use[0]}' === 'Valine' || !!{lazyload}) {
      if (!{lazyload}) btf.loadComment(document.getElementById('vcomment'),loadValine)
      else setTimeout(loadValine, 0)
    } else {
      window.loadOtherComment = loadValine
    }
  })()
```

### 文件路径: `themes\butterfly\layout\includes\third-party\comments\waline.pug`
```pug
- const { serverURL, option, pageview } = theme.waline
- const { lazyload, count, use } = theme.comments

script.
  (() => {
    let initFn = window.walineFn || null
    const isShuoshuo = GLOBAL_CONFIG_SITE.pageType === 'shuoshuo'
    const option = !{JSON.stringify(option)}

    const destroyWaline = ele => ele.destroy()

    const initWaline = (Fn, el = document, path = window.location.pathname) => {
      const waline = Fn({
        el: el.querySelector('#waline-wrap'),
        serverURL: '!{serverURL}',
        pageview: !{lazyload ? false : pageview},
        dark: 'html[data-theme="dark"]',
        comment: !{lazyload ? false : count},
        ...option,
        path: isShuoshuo ? path : (option && option.path) || path
      })

      if (isShuoshuo) {
        window.shuoshuoComment.destroyWaline = () => {
          destroyWaline(waline)
          if (el.children.length) {
            el.innerHTML = ''
            el.classList.add('no-comment')
          }
        }
      }
    }

    const loadWaline = (el, path) => {
      if (initFn) initWaline(initFn, el, path)
      else {
        btf.getCSS('!{url_for(theme.asset.waline_css)}')
          .then(() => import('!{url_for(theme.asset.waline_js)}'))
          .then(({ init }) => {
            initFn = init || Waline.init
            initWaline(initFn, el, path)
            window.walineFn = initFn
          })
      }
    }

    if (isShuoshuo) {
      '!{use[0]}' === 'Waline'
        ? window.shuoshuoComment = { loadComment: loadWaline } 
        : window.loadOtherComment = loadWaline
      return
    }

    if ('!{use[0]}' === 'Waline' || !!{lazyload}) {
      if (!{lazyload}) btf.loadComment(document.getElementById('waline-wrap'),loadWaline)
      else setTimeout(loadWaline, 0)
    } else {
      window.loadOtherComment = loadWaline
    }
  })()


```

### 文件路径: `themes\butterfly\layout\includes\third-party\math\chartjs.pug`
```pug
- const { fontColor, borderColor, scale_ticks_backdropColor } = theme.chartjs

script.
  (() => {
    const applyThemeDefaultsConfig = theme => {
      if (theme === 'dark-mode') {
        Chart.defaults.color = "!{fontColor.dark}"
        Chart.defaults.borderColor = "!{borderColor.dark}"
        Chart.defaults.scale.ticks.backdropColor = "!{scale_ticks_backdropColor.dark}"
      } else {
        Chart.defaults.color = "!{fontColor.light}"
        Chart.defaults.borderColor = "!{borderColor.light}"
        Chart.defaults.scale.ticks.backdropColor = "!{scale_ticks_backdropColor.light}"
      }
    }

    // Recursively traverse the config object and automatically apply theme-specific color schemes
    const applyThemeConfig = (obj, theme) => {
      if (typeof obj !== 'object' || obj === null) return

      Object.keys(obj).forEach(key => {
        const value = obj[key]
        // If the property is an object and has theme-specific options, apply them
        if (typeof value === 'object' && value !== null) {
          if (value[theme]) {
            obj[key] = value[theme] // Apply the value for the current theme
          } else {
            // Recursively process child objects
            applyThemeConfig(value, theme)
          }
        }
      })
    }

    const runChartJS = ele => {
      window.loadChartJS = true

      Array.from(ele).forEach((item, index) => {
        const chartSrc = item.firstElementChild
        const chartID = item.getAttribute('data-chartjs-id') || ('chartjs-' + index) // Use custom ID or default ID
        const width = item.getAttribute('data-width')
        const existingCanvas = document.getElementById(chartID)

        // If a canvas already exists, remove it to avoid rendering duplicates
        if (existingCanvas) {
            existingCanvas.parentNode.remove()
        }

        const chartDefinition = chartSrc.textContent
        const canvas = document.createElement('canvas')
        canvas.id = chartID

        const div = document.createElement('div')
        div.className = 'chartjs-wrap'

        if (width) {
          div.style.width = width
        }

        div.appendChild(canvas)
        chartSrc.insertAdjacentElement('afterend', div)

        const ctx = document.getElementById(chartID).getContext('2d')

        const config = JSON.parse(chartDefinition)

        const theme = document.documentElement.getAttribute('data-theme') === 'dark' ? 'dark-mode' : 'light-mode'

        // Set default styles (initial setup)
        applyThemeDefaultsConfig(theme)

        // Automatically traverse the config and apply dual-mode color schemes
        applyThemeConfig(config, theme)

        new Chart(ctx, config)
      })
    }

    const loadChartJS = () => {
      const chartJSEle = document.querySelectorAll('#article-container .chartjs-container')
      if (chartJSEle.length === 0) return

      window.loadChartJS ? runChartJS(chartJSEle) : btf.getScript('!{url_for(theme.asset.chartjs)}').then(() => runChartJS(chartJSEle))
    }

    // Listen for theme change events
    btf.addGlobalFn('themeChange', loadChartJS, 'chartjs')
    btf.addGlobalFn('encrypt', loadChartJS, 'chartjs')

    window.pjax ? loadChartJS() : document.addEventListener('DOMContentLoaded', loadChartJS)
  })()

```

### 文件路径: `themes\butterfly\layout\includes\third-party\math\index.pug`
```pug
case theme.math.use
  when 'mathjax'
    if (theme.math.per_page && (['post','page'].includes(globalPageType))) || page.mathjax
      include ./mathjax.pug

  when 'katex'
    if (theme.math.per_page && (['post','page'].includes(globalPageType))) || page.katex
      include ./katex.pug

if theme.mermaid.enable
  include ./mermaid.pug

if theme.chartjs.enable
  include ./chartjs.pug
```

### 文件路径: `themes\butterfly\layout\includes\third-party\math\katex.pug`
```pug
script.
  (async () => {
    const showKatex = () => {
      document.querySelectorAll('#article-container .katex').forEach(el => el.classList.add('katex-show'))
    }

    if (!window.katex_js_css) {
      window.katex_js_css = true
      await btf.getCSS('!{url_for(theme.asset.katex)}')
      if (!{theme.math.katex.copy_tex}) {
        await btf.getScript('!{url_for(theme.asset.katex_copytex)}')
      }
    }

    showKatex()
  })()
```

### 文件路径: `themes\butterfly\layout\includes\third-party\math\mathjax.pug`
```pug
//- Mathjax 3
- const { tags, enableMenu } = theme.math.mathjax
script.
  (() => {
    const loadMathjax = () => {
      if (!window.MathJax) {
        window.MathJax = {
          tex: {
            inlineMath: [['$', '$'], ['\\(', '\\)']],
            tags: '!{tags}',
          },
          chtml: {
            scale: 1.1
          },
          options: {
            enableMenu: !{enableMenu},
            renderActions: {
              findScript: [10, doc => {
                for (const node of document.querySelectorAll('script[type^="math/tex"]')) {
                  const display = !!node.type.match(/; *mode=display/)
                  const math = new doc.options.MathItem(node.textContent, doc.inputJax[0], display)
                  const text = document.createTextNode('')
                  node.parentNode.replaceChild(text, node)
                  math.start = {node: text, delim: '', n: 0}
                  math.end = {node: text, delim: '', n: 0}
                  doc.math.push(math)
                }
              }, '']
            }
          }
        }

        const script = document.createElement('script')
        script.src = '!{url_for(theme.asset.mathjax)}'
        script.id = 'MathJax-script'
        script.async = true
        document.head.appendChild(script)
      } else {
        MathJax.startup.document.state(0)
        MathJax.texReset()
        MathJax.typesetPromise()
      }
    }

    btf.addGlobalFn('encrypt', loadMathjax, 'mathjax')
    window.pjax ? loadMathjax() : window.addEventListener('load', loadMathjax)
  })()
```

### 文件路径: `themes\butterfly\layout\includes\third-party\math\mermaid.pug`
```pug
script.
  (() => {
    const runMermaid = ele => {
      window.loadMermaid = true
      const theme = document.documentElement.getAttribute('data-theme') === 'dark' ? '!{theme.mermaid.theme.dark}' : '!{theme.mermaid.theme.light}'

      ele.forEach((item, index) => {
        const mermaidSrc = item.firstElementChild
        const mermaidThemeConfig = `%%{init:{ 'theme':'${theme}'}}%%\n`
        const mermaidID = `mermaid-${index}`
        const mermaidDefinition = mermaidThemeConfig + mermaidSrc.textContent

        const renderFn = mermaid.render(mermaidID, mermaidDefinition)
        const renderMermaid = svg => {
          mermaidSrc.insertAdjacentHTML('afterend', svg)
        }

        // mermaid v9 and v10 compatibility
        typeof renderFn === 'string' ? renderMermaid(renderFn) : renderFn.then(({ svg }) => renderMermaid(svg))
      })
    }

    const codeToMermaid = () => {
      const codeMermaidEle = document.querySelectorAll('pre > code.mermaid')
      if (codeMermaidEle.length === 0) return

      codeMermaidEle.forEach(ele => {
        const preEle = document.createElement('pre')
        preEle.className = 'mermaid-src'
        preEle.hidden = true
        preEle.textContent = ele.textContent
        const newEle = document.createElement('div')
        newEle.className = 'mermaid-wrap'
        newEle.appendChild(preEle)
        ele.parentNode.replaceWith(newEle)
      })
    }

    const loadMermaid = () => {
      if (!{theme.mermaid.code_write}) codeToMermaid()
      const $mermaid = document.querySelectorAll('#article-container .mermaid-wrap')
      if ($mermaid.length === 0) return

      const runMermaidFn = () => runMermaid($mermaid)
      btf.addGlobalFn('themeChange', runMermaidFn, 'mermaid')
      window.loadMermaid ? runMermaidFn() : btf.getScript('!{url_for(theme.asset.mermaid)}').then(runMermaidFn)
    }

    btf.addGlobalFn('encrypt', loadMermaid, 'mermaid')
    window.pjax ? loadMermaid() : document.addEventListener('DOMContentLoaded', loadMermaid)
  })()
```

### 文件路径: `themes\butterfly\layout\includes\third-party\newest-comments\artalk.pug`
```pug
- const { server, site, option } = theme.artalk
- const avatarCdn = (option !== null && option.gravatar && option.gravatar.mirror) || ''
- const avatarDefault = (option !== null && option.gravatar && (option.gravatar.params || option.gravatar.default)) || ''

!= partial("includes/third-party/newest-comments/common.pug", {}, { cache: true })

script.
  window.addEventListener('load', () => {
    const keyName = 'artalk-newest-comments'
    const { changeContent, generateHtml, run } = window.newestComments

    const getAvatarValue = async () => {
      const predefinedAvatarCdn = '!{avatarCdn}'
      const predefinedAvatarDefault = '!{avatarDefault}'

      const avatarDefaultFormat = e => e.startsWith('d=') ? e : `d=${e}`

      if (predefinedAvatarCdn && predefinedAvatarDefault) {
        return { avatarCdn: predefinedAvatarCdn, avatarDefault: avatarDefaultFormat(predefinedAvatarDefault) }
      }

      try {
        const res = await fetch('!{server}/api/v2/conf')
        const result = await res.json()
        const { mirror, params, default: defaults } = result.frontend_conf.gravatar
        const avatarCdn = predefinedAvatarCdn || mirror
        let avatarDefault = avatarDefaultFormat(predefinedAvatarDefault || params || defaults)
        return { avatarCdn, avatarDefault}
      } catch (e) {
        console.error(e)
        return { avatarCdn: predefinedAvatarCdn, avatarDefault: avatarDefaultFormat(predefinedAvatarDefault) }
      }
    }

    const searchParams = new URLSearchParams({
      'site_name': '!{site}',
      'limit': '!{newestCommentsLimit * 2}', // Fetch more comments to filter pending comments
    })

    const getComment = async (ele) => {
      try {
        const res = await fetch(`!{server}/api/v2/stats/latest_comments?${searchParams}`)
        const result = await res.json()
        const { avatarCdn, avatarDefault } = await getAvatarValue()
        const artalk = result.data
          .filter(e => !e.is_pending) // Filter pending comments
          .slice(0, !{newestCommentsLimit}) // Limit the number of comments
          .map(e => {
            const avatar = avatarCdn && e.email_encrypted ? `${avatarCdn}${e.email_encrypted}?${avatarDefault}` : ''
            return {
              'avatar': avatar,
              'content': changeContent(e.content_marked),
              'nick': e.nick,
              'url': e.page_url,
              'date': e.date,
            }
          })
        btf.saveToLocal.set(keyName, JSON.stringify(artalk), !{theme.aside.card_newest_comments.storage}/(60*24))
        generateHtml(artalk, ele)
      } catch (e) {
        console.log(e)
        ele.textContent= "!{_p('aside.card_newest_comments.error')}"
      }
    }

    run(keyName, getComment)
  })
```

### 文件路径: `themes\butterfly\layout\includes\third-party\newest-comments\common.pug`
```pug
script.
  window.newestComments = {
    changeContent: content => {
      if (content === '') return content

      content = content.replace(/<img.*?src="(.*?)"?[^\>]+>/ig, '[!{_p("aside.card_newest_comments.image")}]') // replace image link
      content = content.replace(/<a[^>]+?href=["']?([^"']+)["']?[^>]*>([^<]+)<\/a>/gi, '[!{_p("aside.card_newest_comments.link")}]') // replace url
      content = content.replace(/<pre><code>.*?<\/pre>/gi, '[!{_p("aside.card_newest_comments.code")}]') // replace code
      content = content.replace(/<code>.*?<\/code>/gi, '[!{_p("aside.card_newest_comments.code")}]') // replace code
      content = content.replace(/<[^>]+>/g, "") // remove html tag

      if (content.length > 150) {
        content = content.substring(0, 150) + '...'
      }
      return content
    },

    generateHtml: (array, ele) => {
      let result = ''

      if (array.length) {
        for (let i = 0; i < array.length; i++) {
          result += '<div class="aside-list-item">'

          if (!{theme.aside.card_newest_comments.avatar} && array[i].avatar) {
            const imgAttr = '!{theme.lazyload.enable && !theme.lazyload.native ? "data-lazy-src" : "src"}'
            const lazyloadNative = '!{theme.lazyload.enable && theme.lazyload.native ? "loading=\"lazy\"" : ""}'
            result += `<a href="${array[i].url}" class="thumbnail"><img ${imgAttr}="${array[i].avatar}" alt="${array[i].nick}" ${lazyloadNative}></a>`
          }

          result += `<div class="content">
          <a class="comment" href="${array[i].url}" title="${array[i].content}">${array[i].content}</a>
          <div class="name"><span>${array[i].nick} / </span><time datetime="${array[i].date}">${btf.diffDate(array[i].date, true)}</time></div>
          </div></div>`
        }
      } else {
        result += '!{_p("aside.card_newest_comments.zero")}'
      }

      ele.innerHTML = result
      window.lazyLoadInstance && window.lazyLoadInstance.update()
      window.pjax && window.pjax.refresh(ele)
    },

    newestCommentInit: (name, getComment) => {
      const $dom = document.querySelector('#card-newest-comments .aside-list')
      if ($dom) {
        const data = btf.saveToLocal.get(name)
        if (data) {
          newestComments.generateHtml(JSON.parse(data), $dom)
        } else {
          getComment($dom)
        }
      }
    },

    run: (name, getComment) => {
      newestComments.newestCommentInit(name, getComment)
      btf.addGlobalFn('pjaxComplete', () => newestComments.newestCommentInit(name, getComment), name)
    }
  }
```

### 文件路径: `themes\butterfly\layout\includes\third-party\newest-comments\disqus-comment.pug`
```pug
!= partial("includes/third-party/newest-comments/common.pug", {}, { cache: true })

script.
  window.addEventListener('load', () => {
    const keyName = 'disqus-newest-comments'
    const { changeContent, generateHtml, run } = window.newestComments

    const getComment = ele => {
      fetch('https://disqus.com/api/3.0/forums/listPosts.json?forum=!{forum}&related=thread&limit=!{newestCommentsLimit}&api_key=!{apiKey}')
        .then(response => response.json())
        .then(data => {
          const disqusArray = data.response.map(item => {
            return {
              'avatar': item.author.avatar.cache,
              'content': changeContent(item.message),
              'nick': item.author.name,
              'url': item.url,
              'date': item.createdAt
            }
          })

          btf.saveToLocal.set(keyName, JSON.stringify(disqusArray), !{theme.aside.card_newest_comments.storage}/(60*24))
          generateHtml(disqusArray, ele)
        }).catch(e => {
          console.error(e)
          ele.textContent= "!{_p('aside.card_newest_comments.error')}"
        })
    }

    run(keyName, getComment)
  })




```

### 文件路径: `themes\butterfly\layout\includes\third-party\newest-comments\github-issues.pug`
```pug
!= partial("includes/third-party/newest-comments/common.pug", {}, { cache: true })

script.
  window.addEventListener('load', () => {
    const keyName = 'github-newest-comments'
    const { changeContent, generateHtml, run } = window.newestComments

    const findTrueUrl = (array, ele) => {
      Promise.all(array.map(item =>
        fetch(item.url).then(resp => resp.json()).then(data => {
          let urlArray = data.body ? data.body.match(/(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?/ig) : []
          if (!Array.isArray(urlArray) || urlArray.length === 0) {
            urlArray = [`${data.html_url}`]
          }
          if (data.user.login === 'utterances-bot') {
            return urlArray.pop()
          } else {
            return urlArray.shift()
          }
        })
      )).then(res => {
          array = array.map((i,index)=> {
            return {
              ...i,
              url: res[index]
            }
          })

          btf.saveToLocal.set(keyName, JSON.stringify(array), !{theme.aside.card_newest_comments.storage}/(60*24))
          generateHtml(array, ele)
      });
    }

    const getComment = ele => {
      fetch('https://api.github.com/repos/!{userRepo}/issues/comments?sort=updated&direction=desc&per_page=!{newestCommentsLimit}&page=1',{
        "headers": {
          Accept: 'application/vnd.github.v3.html+json'
        }
      })
        .then(response => response.json())
        .then(data => {
          const githubArray = data.map(item => {
            return {
              'avatar': item.user.avatar_url,
              'content': changeContent(item.body_html || item.body),
              'nick': item.user.login,
              'url': item.issue_url,
              'date': item.updated_at
            }
          })
          findTrueUrl(githubArray, ele)
        }).catch(e => {
          console.error(e)
          ele.textContent= "!{_p('aside.card_newest_comments.error')}"
        })
    }
    run(keyName, getComment)
  })





```

### 文件路径: `themes\butterfly\layout\includes\third-party\newest-comments\index.pug`
```pug
- let { use } = theme.comments

if use
  -
    let forum,apiKey,userRepo
    let { limit:newestCommentsLimit } = theme.aside.card_newest_comments
    if (newestCommentsLimit > 10 || newestCommentsLimit < 1) newestCommentsLimit = 6

  case use[0]
    when 'Valine'
      include ./valine.pug
    when 'Waline'
      include ./waline.pug
    when 'Twikoo'
      include ./twikoo-comment.pug
    when 'Disqus'
      - forum = theme.disqus.shortname
      - apiKey = theme.disqus.apikey
      include ./disqus-comment.pug
    when 'Disqusjs'
      - forum = theme.disqusjs.shortname
      - apiKey = theme.disqusjs.apikey
      include ./disqus-comment.pug
    when 'Gitalk'
      - let { repo,owner } = theme.gitalk
      - userRepo = owner + '/' + repo
      include ./github-issues.pug
    when 'Utterances'
      - userRepo = theme.utterances.repo
      include ./github-issues.pug
    when 'Remark42'
      include ./remark42.pug
    when 'Artalk'
      include ./artalk.pug
```

### 文件路径: `themes\butterfly\layout\includes\third-party\newest-comments\remark42.pug`
```pug
- const { host, siteId } = theme.remark42
!= partial("includes/third-party/newest-comments/common.pug", {}, { cache: true })

script.
  window.addEventListener('load', () => {
    const keyName = 'remark42-newest-comments'
    const { changeContent, generateHtml, run } = window.newestComments

    const getComment = ele => {
      fetch('!{host}/api/v1/last/!{newestCommentsLimit}?site=!{siteId}')
        .then(response => response.json())
        .then(data => {
          const remark42 = data.map(e => {
            return {
              'avatar': e.user.picture,
              'content': changeContent(e.text),
              'nick': e.user.name,
              'url': e.locator.url,
              'date': e.time,
            }
          })
          btf.saveToLocal.set(keyName, JSON.stringify(remark42), !{theme.aside.card_newest_comments.storage}/(60*24))
          generateHtml(remark42, ele)
        }).catch(e => {
          console.error(e)
          ele.textContent= "!{_p('aside.card_newest_comments.error')}"
        })
    }

    run(keyName, getComment)
  })

```

### 文件路径: `themes\butterfly\layout\includes\third-party\newest-comments\twikoo-comment.pug`
```pug
!= partial("includes/third-party/newest-comments/common.pug", {}, { cache: true })

script.
  window.addEventListener('load', () => {
    const keyName = 'twikoo-newest-comments'
    const { changeContent, generateHtml, run } = window.newestComments

    const getComment = ele => {
      const runTwikoo = () => {
        twikoo.getRecentComments({
          envId: '!{theme.twikoo.envId}',
          region: '!{theme.twikoo.region}',
          pageSize: !{newestCommentsLimit},
          includeReply: true
        }).then(res => {
          const twikooArray = res.map(e => {
            return {
              'content': changeContent(e.comment),
              'avatar': e.avatar,
              'nick': e.nick,
              'url': e.url + '#' + e.id,
              'date': new Date(e.created).toISOString()
            }
          })

          btf.saveToLocal.set(keyName, JSON.stringify(twikooArray), !{theme.aside.card_newest_comments.storage}/(60*24))
          generateHtml(twikooArray, ele)
        }).catch(err => {
          console.error(err)
          ele.textContent= "!{_p('aside.card_newest_comments.error')}"
        })
      }

      if (typeof twikoo === 'object') {
        runTwikoo()
      } else {
        btf.getScript('!{url_for(theme.asset.twikoo)}').then(runTwikoo)
      }
    }

    run(keyName, getComment)
  })




```

### 文件路径: `themes\butterfly\layout\includes\third-party\newest-comments\valine.pug`
```pug
- let default_avatar = theme.valine.avatar

script(src=url_for(theme.asset.blueimp_md5))
!= partial("includes/third-party/newest-comments/common.pug", {}, { cache: true })

script.
  window.addEventListener('load', () => {
    const keyName = 'valine-newest-comments'
    const { changeContent, generateHtml, run } = window.newestComments

    const getIcon = (icon, mail) => {
      if (icon) return icon
      let defaultIcon = '!{ default_avatar ? `?d=${default_avatar}` : ''}'
      let iconUrl = `https://gravatar.loli.net/avatar/${md5(mail.toLowerCase()) + defaultIcon}`
      return iconUrl
    }

    const getComment = ele => {
      const serverURL = '!{theme.valine.serverURLs || `https://${theme.valine.appId.substring(0,8)}.api.lncldglobal.com` }'

      var settings = {
        "method": "GET",
        "headers": {
          "X-LC-Id": '!{theme.valine.appId}',
          "X-LC-Key": '!{theme.valine.appKey}',
          "Content-Type": "application/json"
        },
      }

      fetch(`${serverURL}/1.1/classes/Comment?limit=!{newestCommentsLimit}&order=-createdAt`,settings)
        .then(response => response.json())
        .then(data => {
          const valineArray = data.results.map(e => {
            return {
              'avatar': getIcon(e.QQAvatar, e.mail),
              'content': changeContent(e.comment),
              'nick': e.nick,
              'url': e.url + '#' + e.objectId,
              'date': e.updatedAt,
            }
          })
          btf.saveToLocal.set(keyName, JSON.stringify(valineArray), !{theme.aside.card_newest_comments.storage}/(60*24))
          generateHtml(valineArray, ele)
        }).catch(e => {
          console.error(e)
          ele.textContent= "!{_p('aside.card_newest_comments.error')}"
        })
    }

    run(keyName, getComment)
  })

```

### 文件路径: `themes\butterfly\layout\includes\third-party\newest-comments\waline.pug`
```pug
- const serverURL = theme.waline.serverURL.replace(/\/$/, '')

!= partial("includes/third-party/newest-comments/common.pug", {}, { cache: true })

script.
  window.addEventListener('load', () => {
    const keyName = 'waline-newest-comments'
    const { changeContent, generateHtml, run } = window.newestComments

    const getComment = async (ele) => {
      try {
        const res = await fetch('!{serverURL}/api/comment?type=recent&count=!{newestCommentsLimit}')
        const result = await res.json()
        const walineArray = result.data.map(e => {
          return {
            'content': changeContent(e.comment),
            'avatar': e.avatar,
            'nick': e.nick,
            'url': e.url + '#' + e.objectId,
            'date': e.time || e.insertedAt
          }
        })
        btf.saveToLocal.set(keyName, JSON.stringify(walineArray), !{theme.aside.card_newest_comments.storage}/(60*24))
        generateHtml(walineArray, ele)
      } catch (err) {
        console.error(err)
        ele.textContent= "!{_p('aside.card_newest_comments.error')}"
      }
    }

    run(keyName, getComment)
  })

```

### 文件路径: `themes\butterfly\layout\includes\third-party\search\algolia.pug`
```pug
#algolia-search
  .search-dialog
    nav.search-nav
      span.search-dialog-title= _p('search.title')
      button.search-close-button
        i.fas.fa-times

    .search-wrap
      #algolia-search-input
      hr
      #algolia-search-results
        #algolia-hits
        #algolia-pagination
        #algolia-info
          .algolia-stats
          .algolia-poweredBy

  #search-mask

  script(src=url_for(theme.asset.algolia_search))
  script(src=url_for(theme.asset.instantsearch))
  script(src=url_for(theme.asset.algolia_js))
```

### 文件路径: `themes\butterfly\layout\includes\third-party\search\docsearch.pug`
```pug
- const { placeholder, docsearch: { appId, apiKey, indexName, option } } = theme.search

.docsearch-wrap
  #docsearch(style="display:none")
  link(rel="stylesheet" href=url_for(theme.asset.docsearch_css))
  script(src=url_for(theme.asset.docsearch_js))
  script.
    (() => {
      docsearch(Object.assign({
        appId: '!{appId}',
        apiKey: '!{apiKey}',
        indexName: '!{indexName}',
        container: '#docsearch',
        placeholder: '!{ placeholder || _p("search.input_placeholder")}',
      }, !{JSON.stringify(option)}))

      const handleClick = () => {
        document.querySelector('.DocSearch-Button').click()
      }

      const searchClickFn = () => {
        btf.addEventListenerPjax(document.querySelector('#search-button > .search'), 'click', handleClick)
      }

      searchClickFn()
      window.addEventListener('pjax:complete', searchClickFn)
    })()



```

### 文件路径: `themes\butterfly\layout\includes\third-party\search\index.pug`
```pug
case theme.search.use
  when 'algolia_search'
    include ./algolia.pug
  when 'local_search'
    include ./local-search.pug
  when 'docsearch'
    include ./docsearch.pug
```

### 文件路径: `themes\butterfly\layout\includes\third-party\search\local-search.pug`
```pug
#local-search
  .search-dialog
    nav.search-nav
      span.search-dialog-title= _p('search.title')
      span#loading-status
      button.search-close-button
        i.fas.fa-times

    #loading-database.text-center
      i.fas.fa-spinner.fa-pulse
      span= '  ' + _p("search.load_data")

    .search-wrap
      #local-search-input
        .local-search-box
          input(placeholder=theme.search.placeholder || _p("search.input_placeholder") type="text").local-search-box--input
      hr
      #local-search-results
      #local-search-stats-wrap
  #search-mask

  script(src=url_for(theme.asset.local_search))
```

### 文件路径: `themes\butterfly\layout\includes\third-party\share\addtoany.pug`
```pug
.addtoany
  .a2a_kit.a2a_kit_size_32.a2a_default_style
    - let addtoanyItem = theme.share.addtoany.item.split(',')
    each name in addtoanyItem
      a(class="a2a_button_" + name)

    a.a2a_dd(href="https://www.addtoany.com/share")
script(async src='https://static.addtoany.com/menu/page.js')



```

### 文件路径: `themes\butterfly\layout\includes\third-party\share\index.pug`
```pug
- const { use } = theme.share

if use
  .post-share
    case use
      when 'addtoany'
        !=partial('includes/third-party/share/addtoany', {}, {cache: true})
      when 'sharejs'
        include ./share-js.pug
```

### 文件路径: `themes\butterfly\layout\includes\third-party\share\share-js.pug`
```pug
- const coverVal = page.cover_type === 'img' ? page.cover : theme.avatar.img
.social-share(data-image=url_for(coverVal) data-sites= theme.share.sharejs.sites)
link(rel='stylesheet' href=url_for(theme.asset.sharejs_css) media="print" onload="this.media='all'")
script(src=url_for(theme.asset.sharejs) defer)
```

### 文件路径: `themes\butterfly\layout\includes\widget\card_ad.pug`
```pug
if theme.ad && theme.ad.aside
  .card-widget.ads-wrap
    != theme.ad.aside

```

### 文件路径: `themes\butterfly\layout\includes\widget\card_announcement.pug`
```pug
if theme.aside.card_announcement.enable
  .card-widget.card-announcement
    .item-headline
      i.fas.fa-bullhorn.fa-shake
      span= _p('aside.card_announcement')
    .announcement_content!= theme.aside.card_announcement.content
```

### 文件路径: `themes\butterfly\layout\includes\widget\card_archives.pug`
```pug
if theme.aside.card_archives.enable
  .card-widget.card-archives
    - let type = theme.aside.card_archives.type || 'monthly'
    - let format = theme.aside.card_archives.format || 'MMMM YYYY'
    - let order = theme.aside.card_archives.order || -1
    - let limit = theme.aside.card_archives.limit === 0 ? 0 : theme.aside.card_archives.limit || 8
    != aside_archives({ type:type, format: format, order: order, limit: limit })

```

### 文件路径: `themes\butterfly\layout\includes\widget\card_author.pug`
```pug
if theme.aside.card_author.enable
  .card-widget.card-info.text-center
    .avatar-img
      img(src=url_for(theme.avatar.img) onerror=`this.onerror=null;this.src='` + url_for(theme.error_img.flink) + `'` alt="avatar")
    .author-info-name= config.author
    .author-info-description!= theme.aside.card_author.description || config.description

    .site-data
      a(href=url_for(config.archive_dir) + '/')
        .headline= _p('aside.articles')
        .length-num= site.posts.length
      a(href=url_for(config.tag_dir) + '/')
        .headline= _p('aside.tags')
        .length-num= site.tags.length
      a(href=url_for(config.category_dir) + '/')
        .headline= _p('aside.categories')
        .length-num= site.categories.length

    if theme.aside.card_author.button.enable
      a#card-info-btn(href=theme.aside.card_author.button.link)
        i(class=theme.aside.card_author.button.icon)
        span=theme.aside.card_author.button.text

    if(theme.social)
      .card-info-social-icons
        !=partial('includes/header/social', {}, {cache: true})

```

### 文件路径: `themes\butterfly\layout\includes\widget\card_bottom_self.pug`
```pug
if site.data.widget && site.data.widget.bottom
  each item in site.data.widget.bottom
    .card-widget(class=item.class_name id=item.id_name style=item.order ? `order: ${item.order}` : '')
      .item-headline
        i(class=item.icon)
        span=item.name
      .item-content
        !=item.html


```

### 文件路径: `themes\butterfly\layout\includes\widget\card_categories.pug`
```pug
if theme.aside.card_categories.enable
  if site.categories.length
    .card-widget.card-categories
      !=aside_categories({ limit: theme.aside.card_categories.limit === 0 ? 0 : theme.aside.card_categories.limit || 8 , expand: theme.aside.card_categories.expand })

```

### 文件路径: `themes\butterfly\layout\includes\widget\card_newest_comment.pug`
```pug
if theme.aside.card_newest_comments.enable && theme.comments.use && !['Livere','Facebook Comments','Giscus'].includes(theme.comments.use[0])
  .card-widget#card-newest-comments
    .item-headline
      i.fas.fa-comment-dots
      span= _p('aside.card_newest_comments.headline')
    .aside-list
      span= _p('aside.card_newest_comments.loading_text')

```

### 文件路径: `themes\butterfly\layout\includes\widget\card_post_series.pug`
```pug
if theme.aside.card_post_series.enable
  - const array = fragment_cache('seriesArr', groupPosts)
  .card-widget.card-post-series
    .item-headline
      i.fa-solid.fa-layer-group
      span= theme.aside.card_post_series.series_title ? page.series : _p('aside.card_post_series')
    .aside-list
      each item in array[page.series]
        - const { path, title = _p('no_title'), cover, cover_type, date:dateA } = item
        - let link = url_for(path)
        - let no_cover = cover === false || !theme.cover.aside_enable ? 'no-cover' : ''
        .aside-list-item(class=no_cover)
          if cover && theme.cover.aside_enable
            a.thumbnail(href=link title=title)
              if cover_type === 'img'
                img(src=url_for(cover) onerror=`this.onerror=null;this.src='${url_for(theme.error_img.post_page)}'` alt=title)
              else
                div(style=`background: ${cover}`)
          .content
            a.title(href=link title=title)= title
            time(datetime=date_xml(dateA) title=_p('post.created') + ' ' + full_date(dateA)) #[=date(dateA, config.date_format)]

```

### 文件路径: `themes\butterfly\layout\includes\widget\card_post_toc.pug`
```pug
- let tocNumber = typeof page.toc_number === 'boolean' ? page.toc_number : theme.toc.number
- let tocExpand = typeof page.toc_expand === 'boolean' ? page.toc_expand : theme.toc.expand
- let tocExpandClass = tocExpand ? 'is-expand' : ''

#card-toc.card-widget
  .item-headline
    i.fas.fa-stream
    span= _p('aside.card_toc')
    span.toc-percentage

  if (page.encrypt == true)
    .toc-content.toc-div-class(class=tocExpandClass style="display:none")!=toc(page.origin, {list_number: tocNumber})
  else
    .toc-content(class=tocExpandClass)!=toc(page.content, {list_number: tocNumber})

```

### 文件路径: `themes\butterfly\layout\includes\widget\card_recent_post.pug`
```pug
if theme.aside.card_recent_post.enable
  .card-widget.card-recent-post
    .item-headline
      i.fas.fa-history
      span= _p('aside.card_recent_post')
    .aside-list
      - let postLimit = theme.aside.card_recent_post.limit === 0 ? site.posts.length : theme.aside.card_recent_post.limit || 5
      - let sort = theme.aside.card_recent_post.sort === 'updated' ? 'updated' : 'date'
      - site.posts.sort(sort, -1).limit(postLimit).each(function(article){
        - let link = article.link || article.path
        - let title = article.title || _p('no_title')
        - let no_cover = article.cover === false || !theme.cover.aside_enable ? 'no-cover' : ''
        - let post_cover = article.cover
        .aside-list-item(class=no_cover)
          if post_cover && theme.cover.aside_enable
            a.thumbnail(href=url_for(link) title=title)
              if article.cover_type === 'img'
                img(src=url_for(post_cover) onerror=`this.onerror=null;this.src='${url_for(theme.error_img.post_page)}'` alt=title)
              else
                div(style=`background: ${post_cover}`)
          .content
            a.title(href=url_for(link) title=title)= title
            if theme.aside.card_recent_post.sort === 'updated'
              time(datetime=date_xml(article.updated) title=_p('post.updated') + ' ' + full_date(article.updated)) #[=date(article.updated, config.date_format)]
            else
              time(datetime=date_xml(article.date) title=_p('post.created') + ' ' + full_date(article.date)) #[=date(article.date, config.date_format)]
      - })
```

### 文件路径: `themes\butterfly\layout\includes\widget\card_tags.pug`
```pug
if theme.aside.card_tags.enable
  if site.tags.length
    .card-widget.card-tags
      .item-headline
        i.fas.fa-tags
        span= _p('aside.card_tags')

      - let { limit, orderby, order } = theme.aside.card_tags
      - limit = limit === 0 ? 0 : limit || 40

      if theme.aside.card_tags.color
        .card-tag-cloud!= cloudTags({source: site.tags, orderby: orderby, order: order, minfontsize: 1.15, maxfontsize: 1.45, limit: limit, unit: 'em'})
      else
        .card-tag-cloud!= tagcloud({orderby: orderby, order: order, min_font: 1.1, max_font: 1.5, amount: limit , color: true, start_color: '#999', end_color: '#99a9bf', unit: 'em'})

```

### 文件路径: `themes\butterfly\layout\includes\widget\card_top_self.pug`
```pug
if site.data.widget && site.data.widget.top
  each item in site.data.widget.top
    .card-widget(class=item.class_name id=item.id_name)
      .item-headline
        i(class=item.icon)
        span=item.name
      .item-content
        !=item.html
```

### 文件路径: `themes\butterfly\layout\includes\widget\card_webinfo.pug`
```pug
if theme.aside.card_webinfo.enable
  .card-widget.card-webinfo
    .item-headline
      i.fas.fa-chart-line
      span= _p('aside.card_webinfo.headline')
    .webinfo
      if theme.aside.card_webinfo.post_count
        .webinfo-item
          .item-name= `${_p('aside.card_webinfo.article_name')} :`
          .item-count= site.posts.length
      if theme.aside.card_webinfo.runtime_date
        .webinfo-item
          .item-name= `${_p('aside.card_webinfo.runtime.name')} :`
          .item-count#runtimeshow(data-publishDate=date_xml(theme.aside.card_webinfo.runtime_date))
            i.fa-solid.fa-spinner.fa-spin
      if theme.wordcount.enable && theme.wordcount.total_wordcount
        .webinfo-item
          .item-name= `${_p('aside.card_webinfo.site_wordcount')} :`
          .item-count= totalcount(site)
      if theme.umami_analytics.enable && theme.umami_analytics.UV_PV.site_uv
        .webinfo-item
          .item-name= `${_p('aside.card_webinfo.site_uv_name')} :`
          .item-count#umami-site-uv
            i.fa-solid.fa-spinner.fa-spin
      else if theme.busuanzi.site_uv
        .webinfo-item
          .item-name= `${_p('aside.card_webinfo.site_uv_name')} :`
          .item-count#busuanzi_value_site_uv
            i.fa-solid.fa-spinner.fa-spin
      if theme.umami_analytics.enable && theme.umami_analytics.UV_PV.site_pv
        .webinfo-item
          .item-name= `${_p('aside.card_webinfo.site_pv_name')} :`
          .item-count#umami-site-pv
            i.fa-solid.fa-spinner.fa-spin
      else if theme.busuanzi.site_pv
        .webinfo-item
          .item-name= `${_p('aside.card_webinfo.site_pv_name')} :`
          .item-count#busuanzi_value_site_pv
            i.fa-solid.fa-spinner.fa-spin
      if theme.aside.card_webinfo.last_push_date
        .webinfo-item
          .item-name= `${_p('aside.card_webinfo.last_push_date.name')} :`
          .item-count#last-push-date(data-lastPushDate=date_xml(Date.now()))
            i.fa-solid.fa-spinner.fa-spin
```

### 文件路径: `themes\butterfly\layout\includes\widget\index.pug`
```pug
#aside-content.aside-content
  //- post
  if globalPageType === 'post'
    - const tocStyle = page.toc_style_simple
    - const tocStyleVal = tocStyle === true || tocStyle === false ? tocStyle : theme.toc.style_simple
    if showToc && tocStyleVal
      .sticky_layout
        include ./card_post_toc.pug
    else
      !=partial('includes/widget/card_author', {}, {cache: true})
      !=partial('includes/widget/card_announcement', {}, {cache: true})
      !=partial('includes/widget/card_top_self', {}, {cache: true})
      .sticky_layout
        if showToc
          include ./card_post_toc.pug
        if page.series
          include ./card_post_series.pug
        !=partial('includes/widget/card_recent_post', {}, {cache: true})
        !=partial('includes/widget/card_ad', {}, {cache: true})
  else
    //- page
    !=partial('includes/widget/card_author', {}, {cache: true})
    !=partial('includes/widget/card_announcement', {}, {cache: true})
    !=partial('includes/widget/card_top_self', {}, {cache: true})

    .sticky_layout
      if showToc
        include ./card_post_toc.pug
      !=partial('includes/widget/card_recent_post', {}, {cache: true})
      !=partial('includes/widget/card_ad', {}, {cache: true})
      !=partial('includes/widget/card_newest_comment', {}, {cache: true})
      !=partial('includes/widget/card_categories', {}, {cache: true})
      !=partial('includes/widget/card_tags', {}, {cache: true})
      !=partial('includes/widget/card_archives', {}, {cache: true})
      !=partial('includes/widget/card_webinfo', {}, {cache: true})
      !=partial('includes/widget/card_bottom_self', {}, {cache: true})
```

### 文件路径: `themes\butterfly\scripts\common\postDesc.js`
```js
'use strict'

const { stripHTML, truncate } = require('hexo-util')

// Truncates the given content to a specified length, removing HTML tags and replacing newlines with spaces.
const truncateContent = (content, length) => {
  return truncate(stripHTML(content), { length, separator: ' ' }).replace(/\n/g, ' ')
}

// Generates a post description based on the provided data and theme configuration.
const postDesc = (data, hexo) => {
  const { description, content, postDesc } = data

  if (postDesc) return postDesc

  const { length, method } = hexo.theme.config.index_post_content

  if (method === false) return

  let result
  switch (method) {
    case 1:
      result = description
      break
    case 2:
      result = description || truncateContent(content, length)
      break
    default:
      result = truncateContent(content, length)
  }

  data.postDesc = result
  return result
}

module.exports = { truncateContent, postDesc }

```

### 文件路径: `themes\butterfly\scripts\events\404.js`
```js
/**
 * Butterfly
 * 404 error page
 */

'use strict'

hexo.extend.generator.register('404', function (locals) {
  if (!hexo.theme.config.error_404.enable) return
  return {
    path: '404.html',
    layout: ['page'],
    data: {
      type: '404',
      top_img: false,
      comments: false,
      aside: false
    }
  }
})

```

### 文件路径: `themes\butterfly\scripts\events\cdn.js`
```js
/**
 * Butterfly
 * Merge CDN
 */

'use strict'

const { version } = require('../../package.json')
const path = require('path')

hexo.extend.filter.register('before_generate', () => {
  const themeConfig = hexo.theme.config
  const { CDN } = themeConfig

  const thirdPartySrc = hexo.render.renderSync({ path: path.join(hexo.theme_dir, '/plugins.yml'), engine: 'yaml' })
  const internalSrc = {
    main: {
      name: 'hexo-theme-butterfly',
      file: 'js/main.js',
      version
    },
    utils: {
      name: 'hexo-theme-butterfly',
      file: 'js/utils.js',
      version
    },
    translate: {
      name: 'hexo-theme-butterfly',
      file: 'js/tw_cn.js',
      version
    },
    local_search: {
      name: 'hexo-theme-butterfly',
      file: 'js/search/local-search.js',
      version
    },
    algolia_js: {
      name: 'hexo-theme-butterfly',
      file: 'js/search/algolia.js',
      version
    }
  }

  const minFile = file => {
    return file.replace(/(?<!\.min)\.(js|css)$/g, ext => '.min' + ext)
  }

  const createCDNLink = (data, type, cond = '') => {
    Object.keys(data).forEach(key => {
      let { name, version, file, other_name } = data[key]
      const cdnjs_name = other_name || name
      const cdnjs_file = file.replace(/^[lib|dist]*\/|browser\//g, '')
      const min_cdnjs_file = minFile(cdnjs_file)
      if (cond === 'internal') file = `source/${file}`
      const min_file = minFile(file)
      const verType = CDN.version ? (type === 'local' ? `?v=${version}` : `@${version}`) : ''

      const value = {
        version,
        name,
        file,
        cdnjs_file,
        min_file,
        min_cdnjs_file,
        cdnjs_name
      }

      const cdnSource = {
        local: cond === 'internal' ? `${cdnjs_file + verType}` : `/pluginsSrc/${name}/${file + verType}`,
        jsdelivr: `https://cdn.jsdelivr.net/npm/${name}${verType}/${min_file}`,
        unpkg: `https://unpkg.com/${name}${verType}/${file}`,
        cdnjs: `https://cdnjs.cloudflare.com/ajax/libs/${cdnjs_name}/${version}/${min_cdnjs_file}`,
        custom: (CDN.custom_format || '').replace(/\$\{(.+?)\}/g, (match, $1) => value[$1])
      }

      data[key] = cdnSource[type]
    })

    if (cond === 'internal') data.main_css = 'css/index.css' + (CDN.version ? `?v=${version}` : '')
    return data
  }

  // delete null value
  const deleteNullValue = obj => {
    if (!obj) return
    for (const i in obj) {
      obj[i] === null && delete obj[i]
    }
    return obj
  }

  themeConfig.asset = Object.assign(
    createCDNLink(internalSrc, CDN.internal_provider, 'internal'),
    createCDNLink(thirdPartySrc, CDN.third_party_provider),
    deleteNullValue(CDN.option)
  )
})

```

### 文件路径: `themes\butterfly\scripts\events\comment.js`
```js
/**
 * Capitalize the first letter of comment name
 */

hexo.extend.filter.register('before_generate', () => {
  const themeConfig = hexo.theme.config
  let { use } = themeConfig.comments
  if (!use) return

  // Make sure use is an array
  use = Array.isArray(use) ? use : use.split(',')

  // Capitalize the first letter of each comment name
  use = use.map(item =>
    item.trim().toLowerCase().replace(/\b[a-z]/g, s => s.toUpperCase())
  )

  // Disqus and Disqusjs conflict, only keep the first one
  if (use.includes('Disqus') && use.includes('Disqusjs')) {
    use = [use[0]]
  }

  themeConfig.comments.use = use
})

```

### 文件路径: `themes\butterfly\scripts\events\init.js`
```js
hexo.extend.filter.register('before_generate', () => {
  // Get first two digits of the Hexo version number
  const { version, log, locals } = hexo
  const hexoVer = version.replace(/(^.*\..*)\..*/, '$1')

  if (hexoVer < 5.3) {
    log.error('Please update Hexo to V5.3.0 or higher!')
    log.error('請把 Hexo 升級到 V5.3.0 或更高的版本！')
    process.exit(-1)
  }

  if (locals.get) {
    const data = locals.get('data')
    if (data && data.butterfly) {
      log.error("'butterfly.yml' is deprecated. Please use '_config.butterfly.yml'")
      log.error("'butterfly.yml' 已經棄用，請使用 '_config.butterfly.yml'")
      process.exit(-1)
    }
  }
})

```

### 文件路径: `themes\butterfly\scripts\events\merge_config.js`
```js
const { deepMerge } = require('hexo-util')

hexo.extend.filter.register('before_generate', () => {
  const defaultConfig = {
    nav: {
      logo: null,
      display_title: true,
      fixed: false
    },
    menu: null,
    code_blocks: {
      theme: 'light',
      macStyle: false,
      height_limit: false,
      word_wrap: false,
      copy: true,
      language: true,
      shrink: false,
      fullpage: false
    },
    social: null,
    favicon: '/img/favicon.png',
    avatar: {
      img: '/img/butterfly-icon.png',
      effect: false
    },
    disable_top_img: false,
    default_top_img: null,
    index_img: null,
    archive_img: null,
    tag_img: null,
    tag_per_img: null,
    category_img: null,
    category_per_img: null,
    footer_img: false,
    background: null,
    cover: {
      index_enable: true,
      aside_enable: true,
      archives_enable: true,
      default_cover: null
    },
    error_img: {
      flink: '/img/friend_404.gif',
      post_page: '/img/404.jpg'
    },
    error_404: {
      enable: false,
      subtitle: 'Page Not Found',
      background: '/img/error-page.png'
    },
    post_meta: {
      page: {
        date_type: 'created',
        date_format: 'date',
        categories: true,
        tags: false,
        label: true
      },
      post: {
        position: 'left',
        date_type: 'both',
        date_format: 'date',
        categories: true,
        tags: true,
        label: true
      }
    },
    index_site_info_top: null,
    index_top_img_height: null,
    subtitle: {
      enable: false,
      effect: true,
      typed_option: null,
      source: false,
      sub: null
    },
    index_layout: 3,
    index_post_content: {
      method: 3,
      length: 500
    },
    toc: {
      post: true,
      page: false,
      number: true,
      expand: false,
      style_simple: false,
      scroll_percent: true
    },
    post_copyright: {
      enable: true,
      decode: false,
      author_href: null,
      license: 'CC BY-NC-SA 4.0',
      license_url: 'https://creativecommons.org/licenses/by-nc-sa/4.0/'
    },
    reward: {
      enable: false,
      text: null,
      QR_code: null
    },
    post_edit: {
      enable: false,
      url: null
    },
    related_post: {
      enable: true,
      limit: 6,
      date_type: 'created'
    },
    post_pagination: 1,
    noticeOutdate: {
      enable: false,
      style: 'flat',
      limit_day: 365,
      position: 'top',
      message_prev: 'It has been',
      message_next: 'days since the last update, the content of the article may be outdated.'
    },
    footer: {
      owner: {
        enable: true,
        since: 2019
      },
      custom_text: null,
      copyright: true
    },
    aside: {
      enable: true,
      hide: false,
      button: true,
      mobile: true,
      position: 'right',
      display: {
        archive: true,
        tag: true,
        category: true
      },
      card_author: {
        enable: true,
        description: null,
        button: {
          enable: true,
          icon: 'fab fa-github',
          text: 'Follow Me',
          link: 'https://github.com/xxxxxx'
        }
      },
      card_announcement: {
        enable: true,
        content: 'This is my Blog'
      },
      card_recent_post: {
        enable: true,
        limit: 5,
        sort: 'date',
        sort_order: null
      },
      card_newest_comments: {
        enable: false,
        sort_order: null,
        limit: 6,
        storage: 10,
        avatar: true
      },
      card_categories: {
        enable: true,
        limit: 8,
        expand: 'none',
        sort_order: null
      },
      card_tags: {
        enable: true,
        limit: 40,
        color: false,
        orderby: 'random',
        order: 1,
        sort_order: null
      },
      card_archives: {
        enable: true,
        type: 'monthly',
        format: 'MMMM YYYY',
        order: -1,
        limit: 8,
        sort_order: null
      },
      card_post_series: {
        enable: true,
        series_title: false,
        orderBy: 'date',
        order: -1
      },
      card_webinfo: {
        enable: true,
        post_count: true,
        last_push_date: true,
        sort_order: null,
        runtime_date: null
      }
    },
    rightside_bottom: null,
    translate: {
      enable: false,
      default: '繁',
      defaultEncoding: 2,
      translateDelay: 0,
      msgToTraditionalChinese: '繁',
      msgToSimplifiedChinese: '簡'
    },
    readmode: true,
    darkmode: {
      enable: true,
      button: true,
      autoChangeMode: false,
      start: null,
      end: null
    },
    rightside_scroll_percent: false,
    rightside_item_order: {
      enable: false,
      hide: null,
      show: null
    },
    anchor: {
      auto_update: false,
      click_to_scroll: false
    },
    photofigcaption: false,
    copy: {
      enable: true,
      copyright: {
        enable: false,
        limit_count: 150
      }
    },
    wordcount: {
      enable: false,
      post_wordcount: true,
      min2read: true,
      total_wordcount: true
    },
    busuanzi: {
      site_uv: true,
      site_pv: true,
      page_pv: true
    },
    math: {
      use: null,
      per_page: true,
      hide_scrollbar: false,
      mathjax: {
        enableMenu: true,
        tags: 'none'
      },
      katex: {
        copy_tex: false
      }
    },
    search: {
      use: null,
      placeholder: null,
      algolia_search: {
        hitsPerPage: 6
      },
      local_search: {
        preload: false,
        top_n_per_article: 1,
        unescape: false,
        CDN: null
      },
      docsearch: {
        appId: null,
        apiKey: null,
        indexName: null,
        option: null
      }
    },
    share: {
      use: 'sharejs',
      sharejs: {
        sites: 'facebook,twitter,wechat,weibo,qq'
      },
      addtoany: {
        item: 'facebook,twitter,wechat,sina_weibo,facebook_messenger,email,copy_link'
      }
    },
    comments: {
      use: null,
      text: true,
      lazyload: false,
      count: false,
      card_post_count: false
    },
    disqus: {
      shortname: null,
      apikey: null
    },
    disqusjs: {
      shortname: null,
      apikey: null,
      option: null
    },
    livere: {
      uid: null
    },
    gitalk: {
      client_id: null,
      client_secret: null,
      repo: null,
      owner: null,
      admin: null,
      option: null
    },
    valine: {
      appId: null,
      appKey: null,
      avatar: 'monsterid',
      serverURLs: null,
      bg: null,
      visitor: false,
      option: null
    },
    waline: {
      serverURL: null,
      bg: null,
      pageview: false,
      option: null
    },
    utterances: {
      repo: null,
      issue_term: 'pathname',
      light_theme: 'github-light',
      dark_theme: 'photon-dark',
      js: null,
      option: null
    },
    facebook_comments: {
      app_id: null,
      user_id: null,
      pageSize: 10,
      order_by: 'social',
      lang: 'en_US'
    },
    twikoo: {
      envId: null,
      region: null,
      visitor: false,
      option: null
    },
    giscus: {
      repo: null,
      repo_id: null,
      category_id: null,
      light_theme: 'light',
      dark_theme: 'dark',
      js: null,
      option: null
    },
    remark42: {
      host: null,
      siteId: null,
      option: null
    },
    artalk: {
      server: null,
      site: null,
      visitor: false,
      option: null
    },
    chat: {
      use: null,
      rightside_button: false,
      button_hide_show: false
    },
    chatra: {
      id: null
    },
    tidio: {
      public_key: null
    },
    crisp: {
      website_id: null
    },
    baidu_analytics: null,
    google_analytics: null,
    cloudflare_analytics: null,
    microsoft_clarity: null,
    umami_analytics: {
      enable: false,
      serverURL: null,
      website_id: null,
      option: null,
      UV_PV: {
        site_uv: false,
        site_pv: false,
        page_pv: false,
        token: null
      }
    },
    google_adsense: {
      enable: false,
      auto_ads: true,
      js: 'https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js',
      client: null,
      enable_page_level_ads: true
    },
    ad: {
      index: null,
      aside: null,
      post: null
    },
    site_verification: null,
    category_ui: null,
    tag_ui: null,
    rounded_corners_ui: true,
    text_align_justify: false,
    mask: {
      header: true,
      footer: true
    },
    preloader: {
      enable: false,
      source: 1,
      pace_css_url: null
    },
    enter_transitions: true,
    display_mode: 'light',
    beautify: {
      enable: false,
      field: 'post',
      title_prefix_icon: null,
      title_prefix_icon_color: null
    },
    font: {
      global_font_size: null,
      code_font_size: null,
      font_family: null,
      code_font_family: null
    },
    blog_title_font: {
      font_link: null,
      font_family: null
    },
    hr_icon: {
      enable: true,
      icon: null,
      icon_top: null
    },
    activate_power_mode: {
      enable: false,
      colorful: true,
      shake: true,
      mobile: false
    },
    canvas_ribbon: {
      enable: false,
      size: 150,
      alpha: 0.6,
      zIndex: -1,
      click_to_change: false,
      mobile: false
    },
    canvas_fluttering_ribbon: {
      enable: false,
      mobile: false
    },
    canvas_nest: {
      enable: false,
      color: '0,0,255',
      opacity: 0.7,
      zIndex: -1,
      count: 99,
      mobile: false
    },
    fireworks: {
      enable: false,
      zIndex: 9999,
      mobile: false
    },
    click_heart: {
      enable: false,
      mobile: false
    },
    clickShowText: {
      enable: false,
      text: null,
      fontSize: '15px',
      random: false,
      mobile: false
    },
    lightbox: null,
    series: {
      enable: false,
      orderBy: 'title',
      order: 1,
      number: true
    },
    abcjs: {
      enable: false,
      per_page: true
    },
    mermaid: {
      enable: false,
      code_write: false,
      theme: {
        light: 'default',
        dark: 'dark'
      }
    },
    chartjs: {
      enable: false,
      fontColor: {
        light: 'rgba(0, 0, 0, 0.8)',
        dark: 'rgba(255, 255, 255, 0.8)'
      },
      borderColor: {
        light: 'rgba(0, 0, 0, 0.1)',
        dark: 'rgba(255, 255, 255, 0.2)'
      },
      scale_ticks_backdropColor: {
        light: 'transparent',
        dark: 'transparent'
      }
    },
    note: {
      style: 'flat',
      icons: true,
      border_radius: 3,
      light_bg_offset: 0
    },
    pjax: {
      enable: false,
      exclude: null
    },
    aplayerInject: {
      enable: false,
      per_page: true
    },
    snackbar: {
      enable: false,
      position: 'bottom-left',
      bg_light: '#49b1f5',
      bg_dark: '#1f1f1f'
    },
    instantpage: false,
    lazyload: {
      enable: false,
      native: false,
      field: 'site',
      placeholder: null,
      blur: false
    },
    pwa: {
      enable: false,
      manifest: null,
      apple_touch_icon: null,
      favicon_32_32: null,
      favicon_16_16: null,
      mask_icon: null
    },
    Open_Graph_meta: {
      enable: true,
      option: null
    },
    structured_data: true,
    css_prefix: true,
    inject: {
      head: null,
      bottom: null
    },
    CDN: {
      internal_provider: 'local',
      third_party_provider: 'jsdelivr',
      version: false,
      custom_format: null,
      option: null
    }
  }

  hexo.theme.config = deepMerge(defaultConfig, hexo.theme.config)
}, 1)

```

### 文件路径: `themes\butterfly\scripts\events\stylus.js`
```js
/**
 * Stylus renderer
 */

'use strict'

hexo.extend.filter.register('stylus:renderer', style => {
  const { syntax_highlighter: syntaxHighlighter, highlight, prismjs } = hexo.config
  let { enable: highlightEnable, line_number: highlightLineNumber } = highlight
  let { enable: prismjsEnable, line_number: prismjsLineNumber } = prismjs

  // for hexo > 7.0
  if (syntaxHighlighter) {
    highlightEnable = syntaxHighlighter === 'highlight.js'
    prismjsEnable = syntaxHighlighter === 'prismjs'
  }

  style.define('$highlight_enable', highlightEnable)
    .define('$highlight_line_number', highlightLineNumber)
    .define('$prismjs_enable', prismjsEnable)
    .define('$prismjs_line_number', prismjsLineNumber)
    .define('$language', hexo.config.language)
  // .import(`${this.source_dir.replace(/\\/g, '/')}_data/css/*`)
})

```

### 文件路径: `themes\butterfly\scripts\events\welcome.js`
```js
hexo.on('ready', () => {
  const { version } = require('../../package.json')
  hexo.log.info(`
  ===================================================================
      #####  #    # ##### ##### ###### #####  ###### #      #   #
      #    # #    #   #     #   #      #    # #      #       # #
      #####  #    #   #     #   #####  #    # #####  #        #
      #    # #    #   #     #   #      #####  #      #        #
      #    # #    #   #     #   #      #   #  #      #        #
      #####   ####    #     #   ###### #    # #      ######   #
                            ${version}
  ===================================================================`)
})

```

### 文件路径: `themes\butterfly\scripts\filters\post_lazyload.js`
```js
/**
 * Butterfly
 * lazyload
 * replace src to data-lazy-src
 */

'use strict'

const urlFor = require('hexo-util').url_for.bind(hexo)

const lazyload = htmlContent => {
  if (hexo.theme.config.lazyload.native) {
    return htmlContent.replace(/(<img.*?)(>)/ig, '$1 loading=\'lazy\'$2')
  }

  const bg = hexo.theme.config.lazyload.placeholder ? urlFor(hexo.theme.config.lazyload.placeholder) : 'data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7'
  return htmlContent.replace(/(<img.*? src=)/ig, `$1 "${bg}" data-lazy-src=`)
}

hexo.extend.filter.register('after_render:html', data => {
  const { enable, field } = hexo.theme.config.lazyload
  if (!enable || field !== 'site') return
  return lazyload(data)
})

hexo.extend.filter.register('after_post_render', data => {
  const { enable, field } = hexo.theme.config.lazyload
  if (!enable || field !== 'post') return
  data.content = lazyload(data.content)
  return data
})

```

### 文件路径: `themes\butterfly\scripts\filters\random_cover.js`
```js
/**
 * Random cover for posts
 */

'use strict'

hexo.extend.generator.register('post', locals => {
  const previousIndexes = []

  const getRandomCover = defaultCover => {
    if (!defaultCover) return false
    if (!Array.isArray(defaultCover)) return defaultCover

    const coverCount = defaultCover.length

    if (coverCount === 1) {
      return defaultCover[0]
    }

    const maxPreviousIndexes = coverCount === 2 ? 1 : (coverCount === 3 ? 2 : 3)

    let index
    do {
      index = Math.floor(Math.random() * coverCount)
    } while (previousIndexes.includes(index) && previousIndexes.length < coverCount)

    previousIndexes.push(index)
    if (previousIndexes.length > maxPreviousIndexes) {
      previousIndexes.shift()
    }

    return defaultCover[index]
  }

  const handleImg = data => {
    const imgTestReg = /\.(png|jpe?g|gif|svg|webp|avif)(\?.*)?$/i
    let { cover: coverVal, top_img: topImg } = data

    // Add path to top_img and cover if post_asset_folder is enabled
    if (hexo.config.post_asset_folder) {
      if (topImg && topImg.indexOf('/') === -1 && imgTestReg.test(topImg)) {
        data.top_img = `${data.path}${topImg}`
      }
      if (coverVal && coverVal.indexOf('/') === -1 && imgTestReg.test(coverVal)) {
        data.cover = `${data.path}${coverVal}`
      }
    }

    if (coverVal === false) return data

    // If cover is not set, use random cover
    if (!coverVal) {
      const { cover: { default_cover: defaultCover } } = hexo.theme.config
      const randomCover = getRandomCover(defaultCover)
      data.cover = randomCover
      coverVal = randomCover // update coverVal
    }

// 修复 coverVal 类型错误
if (!Array.isArray(coverVal)) coverVal = [];  // 确保 coverVal 是数组

if (coverVal.some(item => 
  item.includes('//') || imgTestReg.test(item)
)) {
  data.cover_type = 'img';
}

    return data
  }

  // https://github.com/hexojs/hexo/blob/master/lib%2Fplugins%2Fgenerator%2Fpost.ts
  const posts = locals.posts.sort('date').toArray()
  const { length } = posts

  return posts.map((post, i) => {
    if (i) post.prev = posts[i - 1]
    if (i < length - 1) post.next = posts[i + 1]

    post.__post = true

    return {
      data: handleImg(post),
      layout: 'post',
      path: post.path
    }
  })
})

```

### 文件路径: `themes\butterfly\scripts\filters\random_cover.js.bak`
```bak
/**
 * Random cover for posts
 */

'use strict'

hexo.extend.generator.register('post', locals => {
  const previousIndexes = []

  const getRandomCover = defaultCover => {
    if (!defaultCover) return false
    if (!Array.isArray(defaultCover)) return defaultCover

    const coverCount = defaultCover.length

    if (coverCount === 1) {
      return defaultCover[0]
    }

    const maxPreviousIndexes = coverCount === 2 ? 1 : (coverCount === 3 ? 2 : 3)

    let index
    do {
      index = Math.floor(Math.random() * coverCount)
    } while (previousIndexes.includes(index) && previousIndexes.length < coverCount)

    previousIndexes.push(index)
    if (previousIndexes.length > maxPreviousIndexes) {
      previousIndexes.shift()
    }

    return defaultCover[index]
  }

  const handleImg = data => {
    const imgTestReg = /\.(png|jpe?g|gif|svg|webp|avif)(\?.*)?$/i
    let { cover: coverVal, top_img: topImg } = data

    // Add path to top_img and cover if post_asset_folder is enabled
    if (hexo.config.post_asset_folder) {
      if (topImg && topImg.indexOf('/') === -1 && imgTestReg.test(topImg)) {
        data.top_img = `${data.path}${topImg}`
      }
      if (coverVal && coverVal.indexOf('/') === -1 && imgTestReg.test(coverVal)) {
        data.cover = `${data.path}${coverVal}`
      }
    }

    if (coverVal === false) return data

    // If cover is not set, use random cover
    if (!coverVal) {
      const { cover: { default_cover: defaultCover } } = hexo.theme.config
      const randomCover = getRandomCover(defaultCover)
      data.cover = randomCover
      coverVal = randomCover // update coverVal
    }

    if (coverVal && (coverVal.indexOf('//') !== -1 || imgTestReg.test(coverVal))) {
      data.cover_type = 'img'
    }

    return data
  }

  // https://github.com/hexojs/hexo/blob/master/lib%2Fplugins%2Fgenerator%2Fpost.ts
  const posts = locals.posts.sort('date').toArray()
  const { length } = posts

  return posts.map((post, i) => {
    if (i) post.prev = posts[i - 1]
    if (i < length - 1) post.next = posts[i + 1]

    post.__post = true

    return {
      data: handleImg(post),
      layout: 'post',
      path: post.path
    }
  })
})

```

### 文件路径: `themes\butterfly\scripts\helpers\aside_archives.js`
```js
'use strict'

hexo.extend.helper.register('aside_archives', function (options = {}) {
  const { config, page, site, url_for, _p } = this
  const {
    archive_dir: archiveDir,
    timezone,
    language
  } = config

  // Destructure and set default options with object destructuring
  const {
    type = 'monthly',
    format = type === 'monthly' ? 'MMMM YYYY' : 'YYYY',
    show_count: showCount = true,
    order = -1,
    limit,
    transform
  } = options

  // Optimize locale handling
  const lang = toMomentLocale(page.lang || page.language || language)

  // Memoize comparison function to improve performance
  const compareFunc = type === 'monthly'
    ? (yearA, monthA, yearB, monthB) => yearA === yearB && monthA === monthB
    : (yearA, yearB) => yearA === yearB

  // Early return if no posts
  if (!site.posts.length) return ''

  // Use reduce for more efficient data processing
  const data = site.posts
    .sort('date', order)
    .reduce((acc, post) => {
      let date = post.date.clone()
      if (timezone) date = date.tz(timezone)

      const year = date.year()
      const month = date.month() + 1

      if (lang) date = date.locale(lang)

      // Find or create archive entry
      const lastEntry = acc[acc.length - 1]
      if (!lastEntry || !compareFunc(
        lastEntry.year,
        lastEntry.month,
        year,
        month
      )) {
        acc.push({
          name: date.format(format),
          year,
          month,
          count: 1
        })
      } else {
        lastEntry.count++
      }

      return acc
    }, [])

  // Create link generator function
  const createArchiveLink = item => {
    let url = `${archiveDir}/${item.year}/`
    if (type === 'monthly') {
      url += item.month < 10 ? `0${item.month}/` : `${item.month}/`
    }
    return url_for(url)
  }

  // Limit results efficiently
  const limitedData = limit > 0
    ? data.slice(0, Math.min(data.length, limit))
    : data

  // Use template literal for better readability
  const archiveHeader = `
    <div class="item-headline">
      <i class="fas fa-archive"></i>
      <span>${_p('aside.card_archives')}</span>
      ${data.length > limitedData.length
        ? `<a class="card-more-btn" href="${url_for(archiveDir)}/"
            title="${_p('aside.more_button')}">
            <i class="fas fa-angle-right"></i>
          </a>`
        : ''}
    </div>
  `

  // Use map for generating list items, join for performance
  const archiveList = `
    <ul class="card-archive-list">
      ${limitedData.map(item => `
        <li class="card-archive-list-item">
          <a class="card-archive-list-link" href="${createArchiveLink(item)}">
            <span class="card-archive-list-date">
              ${transform ? transform(item.name) : item.name}
            </span>
            ${showCount
              ? `<span class="card-archive-list-count">${item.count}</span>`
              : ''}
          </a>
        </li>
      `).join('')}
    </ul>
  `

  return archiveHeader + archiveList
})

// Improved locale conversion function
const toMomentLocale = lang => {
  if (!lang || ['en', 'default'].includes(lang)) return 'en'
  return lang.toLowerCase().replace('_', '-')
}

```

### 文件路径: `themes\butterfly\scripts\helpers\aside_categories.js`
```js
'use strict'

hexo.extend.helper.register('aside_categories', function (categories, options = {}) {
  if (!categories || !Object.prototype.hasOwnProperty.call(categories, 'length')) {
    options = categories || {}
    categories = this.site.categories
  }

  if (!categories || !categories.length) return ''

  const { config } = this
  const showCount = Object.prototype.hasOwnProperty.call(options, 'show_count') ? options.show_count : true
  const depth = options.depth ? parseInt(options.depth, 10) : 0
  const orderby = options.orderby || 'name'
  const order = options.order || 1
  const categoryDir = this.url_for(config.category_dir)
  const limit = options.limit === 0 ? categories.length : (options.limit || categories.length)
  const isExpand = options.expand !== 'none'
  const expandClass = isExpand && options.expand === true ? 'expand' : ''
  const buttonLabel = this._p('aside.more_button')

  const prepareQuery = parent => {
    const query = parent ? { parent } : { parent: { $exists: false } }
    return categories.find(query).sort(orderby, order).filter(cat => cat.length)
  }

  const hierarchicalList = (remaining, level = 0, parent) => {
    let result = ''
    if (remaining > 0) {
      prepareQuery(parent).forEach(cat => {
        if (remaining > 0) {
          remaining -= 1
          let child = ''
          if (!depth || level + 1 < depth) {
            const childList = hierarchicalList(remaining, level + 1, cat._id)
            child = childList.result
            remaining = childList.remaining
          }

          const parentClass = isExpand && !parent && child ? 'parent' : ''
          result += `<li class="card-category-list-item ${parentClass}">`
          result += `<a class="card-category-list-link" href="${this.url_for(cat.path)}">`
          result += `<span class="card-category-list-name">${cat.name}</span>`

          if (showCount) {
            result += `<span class="card-category-list-count">${cat.length}</span>`
          }

          if (isExpand && !parent && child) {
            result += `<i class="fas fa-caret-left ${expandClass}"></i>`
          }

          result += '</a>'

          if (child) {
            result += `<ul class="card-category-list child">${child}</ul>`
          }

          result += '</li>'
        }
      })
    }
    return { result, remaining }
  }

  const list = hierarchicalList(limit)

  const moreButton = categories.length > limit
    ? `<a class="card-more-btn" href="${categoryDir}/" title="${buttonLabel}">
      <i class="fas fa-angle-right"></i></a>`
    : ''

  return `<div class="item-headline">
            <i class="fas fa-folder-open"></i>
            <span>${this._p('aside.card_categories')}</span>
            ${moreButton}
          </div>
          <ul class="card-category-list${isExpand && list.result ? ' expandBtn' : ''}" id="aside-cat-list">
            ${list.result}
          </ul>`
})

```

### 文件路径: `themes\butterfly\scripts\helpers\getArchiveLength.js`
```js
hexo.extend.helper.register('getArchiveLength', function () {
  const archiveGenerator = hexo.config.archive_generator
  const posts = this.site.posts

  const { yearly, monthly, daily } = archiveGenerator
  const { year, month, day } = this.page

  // Archives Page
  if (!year) return posts.length

  // Function to generate a unique key based on the granularity
  const getKey = (post, type) => {
    const date = post.date.clone()
    const y = date.year()
    const m = date.month() + 1
    const d = date.date()
    if (type === 'year') return `${y}`
    if (type === 'month') return `${y}-${m}`
    if (type === 'day') return `${y}-${m}-${d}`
  }

  // Create a map to count posts per period
  const mapData = this.fragment_cache('createArchiveObj', () => {
    const map = new Map()
    posts.forEach(post => {
      const keyYear = getKey(post, 'year')
      const keyMonth = getKey(post, 'month')
      const keyDay = getKey(post, 'day')

      if (yearly) map.set(keyYear, (map.get(keyYear) || 0) + 1)
      if (monthly) map.set(keyMonth, (map.get(keyMonth) || 0) + 1)
      if (daily) map.set(keyDay, (map.get(keyDay) || 0) + 1)
    })
    return map
  })

  // Determine the appropriate key to fetch based on current page context
  let key
  if (yearly && year) key = `${year}`
  if (monthly && month) key = `${year}-${month}`
  if (daily && day) key = `${year}-${month}-${day}`

  // Return the count for the current period or default to the total posts
  return mapData.get(key) || posts.length
})

```

### 文件路径: `themes\butterfly\scripts\helpers\inject_head_js.js`
```js
'use strict'

hexo.extend.helper.register('inject_head_js', function () {
  const { darkmode, aside, pjax } = this.theme
  const start = darkmode.start || 6
  const end = darkmode.end || 18
  const { theme_color } = hexo.theme.config
  const themeColorLight = theme_color && theme_color.enable ? theme_color.meta_theme_color_light : '#ffffff'
  const themeColorDark = theme_color && theme_color.enable ? theme_color.meta_theme_color_dark : '#0d0d0d'

  const createCustomJs = () => `
    const saveToLocal = {
      set: (key, value, ttl) => {
        if (!ttl) return
        const expiry = Date.now() + ttl * 86400000
        localStorage.setItem(key, JSON.stringify({ value, expiry }))
      },
      get: key => {
        const itemStr = localStorage.getItem(key)
        if (!itemStr) return undefined
        const { value, expiry } = JSON.parse(itemStr)
        if (Date.now() > expiry) {
          localStorage.removeItem(key)
          return undefined
        }
        return value
      }
    }

    window.btf = {
      saveToLocal,
      getScript: (url, attr = {}) => new Promise((resolve, reject) => {
        const script = document.createElement('script')
        script.src = url
        script.async = true
        Object.entries(attr).forEach(([key, val]) => script.setAttribute(key, val))
        script.onload = script.onreadystatechange = () => {
          if (!script.readyState || /loaded|complete/.test(script.readyState)) resolve()
        }
        script.onerror = reject
        document.head.appendChild(script)
      }),
      getCSS: (url, id) => new Promise((resolve, reject) => {
        const link = document.createElement('link')
        link.rel = 'stylesheet'
        link.href = url
        if (id) link.id = id
        link.onload = link.onreadystatechange = () => {
          if (!link.readyState || /loaded|complete/.test(link.readyState)) resolve()
        }
        link.onerror = reject
        document.head.appendChild(link)
      }),
      addGlobalFn: (key, fn, name = false, parent = window) => {
        if (!${pjax.enable} && key.startsWith('pjax')) return
        const globalFn = parent.globalFn || {}
        globalFn[key] = globalFn[key] || {}
        globalFn[key][name || Object.keys(globalFn[key]).length] = fn
        parent.globalFn = globalFn
      }
    }
  `

  const createDarkmodeJs = () => {
    if (!darkmode.enable) return ''

    let darkmodeJs = `
      const activateDarkMode = () => {
        document.documentElement.setAttribute('data-theme', 'dark')
        if (document.querySelector('meta[name="theme-color"]') !== null) {
          document.querySelector('meta[name="theme-color"]').setAttribute('content', '${themeColorDark}')
        }
      }
      const activateLightMode = () => {
        document.documentElement.setAttribute('data-theme', 'light')
        if (document.querySelector('meta[name="theme-color"]') !== null) {
          document.querySelector('meta[name="theme-color"]').setAttribute('content', '${themeColorLight}')
        }
      }

      btf.activateDarkMode = activateDarkMode
      btf.activateLightMode = activateLightMode

      const theme = saveToLocal.get('theme')
    `

    switch (darkmode.autoChangeMode) {
      case 1:
        darkmodeJs += `
          const mediaQueryDark = window.matchMedia('(prefers-color-scheme: dark)')
          const mediaQueryLight = window.matchMedia('(prefers-color-scheme: light)')
          
          if (theme === undefined) {
            if (mediaQueryLight.matches) activateLightMode()
            else if (mediaQueryDark.matches) activateDarkMode()
            else {
              const hour = new Date().getHours()
              const isNight = hour <= ${start} || hour >= ${end}
              isNight ? activateDarkMode() : activateLightMode()
            }
            mediaQueryDark.addEventListener('change', () => {
              if (saveToLocal.get('theme') === undefined) {
                e.matches ? activateDarkMode() : activateLightMode()
              }
            })
          } else {
            theme === 'light' ? activateLightMode() : activateDarkMode()
          }
        `
        break
      case 2:
        darkmodeJs += `
          const hour = new Date().getHours()
          const isNight = hour <= ${start} || hour >= ${end}
          if (theme === undefined) isNight ? activateDarkMode() : activateLightMode()
          else theme === 'light' ? activateLightMode() : activateDarkMode()
        `
        break
      default:
        darkmodeJs += `
          theme === 'dark' ? activateDarkMode() : theme === 'light' ? activateLightMode() : null
        `
    }

    return darkmodeJs
  }

  const createAsideStatusJs = () => {
    if (!aside.enable || !aside.button) return ''
    return `
      const asideStatus = saveToLocal.get('aside-status')
      if (asideStatus !== undefined) {
        document.documentElement.classList.toggle('hide-aside', asideStatus === 'hide')
      }
    `
  }

  const createDetectAppleJs = () => `
    const detectApple = () => {
      if (/iPad|iPhone|iPod|Macintosh/.test(navigator.userAgent)) {
        document.documentElement.classList.add('apple')
      }
    }
    detectApple()
  `

  return `<script>
    (() => {
      ${createCustomJs()}
      ${createDarkmodeJs()}
      ${createAsideStatusJs()}
      ${createDetectAppleJs()}
    })()
  </script>`
})

```

### 文件路径: `themes\butterfly\scripts\helpers\page.js`
```js
'use strict'

const { truncateContent, postDesc } = require('../common/postDesc')
const { prettyUrls } = require('hexo-util')
const crypto = require('crypto')
const moment = require('moment-timezone')

hexo.extend.helper.register('truncate', truncateContent)

hexo.extend.helper.register('postDesc', data => {
  return postDesc(data, hexo)
})

hexo.extend.helper.register('cloudTags', function (options = {}) {
  const env = this
  let { source, minfontsize, maxfontsize, limit, unit = 'px', orderby, order } = options

  if (limit > 0) {
    source = source.limit(limit)
  }

  const sizes = [...new Set(source.map(tag => tag.length).sort((a, b) => a - b))]

  const getRandomColor = () => {
    const randomColor = () => Math.floor(Math.random() * 201)
    const r = randomColor()
    const g = randomColor()
    const b = randomColor()
    return `rgb(${Math.max(r, 50)}, ${Math.max(g, 50)}, ${Math.max(b, 50)})`
  }

  const generateStyle = (size, unit) =>
    `font-size: ${parseFloat(size.toFixed(2)) + unit}; color: ${getRandomColor()};`

  const length = sizes.length - 1
  const result = source.sort(orderby, order).map(tag => {
    const ratio = length ? sizes.indexOf(tag.length) / length : 0
    const size = minfontsize + ((maxfontsize - minfontsize) * ratio)
    const style = generateStyle(size, unit)
    return `<a href="${env.url_for(tag.path)}" style="${style}">${tag.name}</a>`
  }).join('')

  return result
})

hexo.extend.helper.register('urlNoIndex', function (url = null, trailingIndex = false, trailingHtml = false) {
  return prettyUrls(url || this.url, { trailing_index: trailingIndex, trailing_html: trailingHtml })
})

hexo.extend.helper.register('md5', function (path) {
  return crypto.createHash('md5').update(decodeURI(this.url_for(path))).digest('hex')
})

hexo.extend.helper.register('injectHtml', data => {
  return data ? data.join('') : ''
})

hexo.extend.helper.register('findArchivesTitle', function (page, menu, date) {
  if (page.year) {
    const dateStr = page.month ? `${page.year}-${page.month}` : `${page.year}`
    const dateFormat = page.month ? hexo.theme.config.aside.card_archives.format : 'YYYY'
    return date(dateStr, dateFormat)
  }

  const defaultTitle = this._p('page.archives')
  if (!menu) return defaultTitle

  const loop = (m) => {
    for (const key in m) {
      if (typeof m[key] === 'object') {
        const result = loop(m[key])
        if (result) return result
      }

      if (/\/archives\//.test(m[key])) {
        return key
      }
    }
  }

  return loop(menu) || defaultTitle
})

hexo.extend.helper.register('getBgPath', path => {
  if (!path) return ''

  const absoluteUrlPattern = /^(?:[a-z][a-z\d+.-]*:)?\/\//i
  const relativeUrlPattern = /^(\.\/|\.\.\/|\/|[^/]+\/).*$/
  const colorPattern = /^(#|rgb|rgba|hsl|hsla)/i

  if (colorPattern.test(path)) {
    return `background-color: ${path};`
  } else if (absoluteUrlPattern.test(path) || relativeUrlPattern.test(path)) {
    return `background-image: url(${path});`
  } else {
    return `background: ${path};`
  }
})

hexo.extend.helper.register('shuoshuoFN', (data, page) => {
  const { limit } = page
  let finalResult = ''

  // Check if limit.value is a valid date
  const isValidDate = date => !isNaN(Date.parse(date))

  // order by date
  const orderByDate = data => data.sort((a, b) => Date.parse(b.date) - Date.parse(a.date))

  // Apply number limit or time limit conditionally
  const limitData = data => {
    if (limit && limit.type === 'num' && limit.value > 0) {
      return data.slice(0, limit.value)
    } else if (limit && limit.type === 'date' && isValidDate(limit.value)) {
      const limitDate = Date.parse(limit.value)
      return data.filter(item => Date.parse(item.date) >= limitDate)
    }

    return data
  }

  orderByDate(data)
  finalResult = limitData(data)

  // This is a hack method, because hexo treats time as UTC time
  // so you need to manually convert the time zone
  finalResult.forEach(item => {
    const utcDate = moment.utc(item.date).format('YYYY-MM-DD HH:mm:ss')
    item.date = moment.tz(utcDate, hexo.config.timezone).format('YYYY-MM-DD HH:mm:ss')
  })

  return finalResult
})

hexo.extend.helper.register('getPageType', (page, isHome) => {
  const { layout, tag, category, type, archive } = page
  if (layout) return layout
  if (tag) return 'tag'
  if (category) return 'category'
  if (archive) return 'archive'
  if (type) {
    if (type === 'tags' || type === 'categories') return type
    else return 'page'
  }
  if (isHome) return 'home'
  return 'post'
})

hexo.extend.helper.register('getVersion', () => {
  const { version } = require('../../package.json')
  return { hexo: hexo.version, theme: version }
})

```

### 文件路径: `themes\butterfly\scripts\helpers\related_post.js`
```js
/* eslint-disable camelcase */
/**
 * Butterfly
 * Related Posts
 * According the tag
 */

'use strict'

const { postDesc } = require('../common/postDesc')

hexo.extend.helper.register('related_posts', function (currentPost, allPosts) {
  let relatedPosts = []
  const tagsData = currentPost.tags
  tagsData.length && tagsData.forEach(function (tag) {
    allPosts.forEach(function (post) {
      if (currentPost.path !== post.path && isTagRelated(tag.name, post.tags)) {
        const getPostDesc = post.postDesc || postDesc(post, hexo)
        const relatedPost = {
          title: post.title,
          path: post.path,
          cover: post.cover,
          cover_type: post.cover_type,
          weight: 1,
          updated: post.updated,
          created: post.date,
          postDesc: getPostDesc
        }
        const index = findItem(relatedPosts, 'path', post.path)
        if (index !== -1) {
          relatedPosts[index].weight += 1
        } else {
          relatedPosts.push(relatedPost)
        }
      }
    })
  })

  if (relatedPosts.length === 0) {
    return ''
  }
  let result = ''
  const hexoConfig = hexo.config
  const config = hexo.theme.config

  const limitNum = config.related_post.limit || 6
  const dateType = config.related_post.date_type || 'created'
  const headlineLang = this._p('post.recommend')

  relatedPosts = relatedPosts.sort(compare('weight'))

  if (relatedPosts.length > 0) {
    result += '<div class="relatedPosts">'
    result += `<div class="headline"><i class="fas fa-thumbs-up fa-fw"></i><span>${headlineLang}</span></div>`
    result += '<div class="relatedPosts-list">'

    for (let i = 0; i < Math.min(relatedPosts.length, limitNum); i++) {
      let { cover, title, path, cover_type, created, updated, postDesc } = relatedPosts[i]
      const { escape_html, url_for, date } = this
      cover = cover || 'var(--default-bg-color)'
      title = escape_html(title)
      const className = postDesc ? 'pagination-related' : 'pagination-related no-desc'
      result += `<a class="${className}" href="${url_for(path)}" title="${title}">`
      if (cover_type === 'img') {
        result += `<img class="cover" src="${url_for(cover)}" alt="cover">`
      } else {
        result += `<div class="cover" style="background: ${cover}"></div>`
      }
      if (dateType === 'created') {
        result += `<div class="info text-center"><div class="info-1"><div class="info-item-1"><i class="far fa-calendar-alt fa-fw"></i> ${date(created, hexoConfig.date_format)}</div>`
      } else {
        result += `<div class="info text-center"><div class="info-1"><div class="info-item-1"><i class="fas fa-history fa-fw"></i> ${date(updated, hexoConfig.date_format)}</div>`
      }
      result += `<div class="info-item-2">${title}</div></div>`

      if (postDesc) {
        result += `<div class="info-2"><div class="info-item-1">${postDesc}</div></div>`
      }
      result += '</div></a>'
    }

    result += '</div></div>'
    return result
  }
})

function isTagRelated (tagName, tags) {
  return tags.some(tag => tag.name === tagName)
}

function findItem (arrayToSearch, attr, val) {
  return arrayToSearch.findIndex(item => item[attr] === val)
}

function compare (attr) {
  return (a, b) => b[attr] - a[attr]
}

```

### 文件路径: `themes\butterfly\scripts\helpers\series.js`
```js
'use strict'

hexo.extend.helper.register('groupPosts', function () {
  const getGroupArray = array => {
    return array.reduce((groups, item) => {
      const key = item.series
      if (key) {
        groups[key] = groups[key] || []
        groups[key].push(item)
      }
      return groups
    }, {})
  }

  const sortPosts = posts => {
    const { orderBy = 'date', order = 1 } = this.theme.aside.card_post_series
    if (orderBy === 'title') return posts.sort('title', order)
    return posts.sort('date', order)
  }

  return getGroupArray(sortPosts(this.site.posts))
})

```

### 文件路径: `themes\butterfly\scripts\tag\button.js`
```js
/**
 * Button
 * {% btn url text icon option %}
 * option: color outline center block larger
 * color : default/blue/pink/red/purple/orange/green
 */

'use strict'

const urlFor = require('hexo-util').url_for.bind(hexo)

const btn = args => {
  const [url = '', text = '', icon = '', option = ''] = args.join(' ').split(',').map(arg => arg.trim())

  const iconHTML = icon ? `<i class="${icon}"></i>` : ''
  const textHTML = text ? `<span>${text}</span>` : ''

  return `<a class="btn-beautify ${option}" href="${urlFor(url)}" title="${text}">${iconHTML}${textHTML}</a>`
}

hexo.extend.tag.register('btn', btn, { ends: false })

```

### 文件路径: `themes\butterfly\scripts\tag\chartjs.js`
```js
/**
 * Butterfly
 * chartjs
 * https://www.chartjs.org/
 * {% chartjs [width, abreast, chartId] %}
 * <!-- chart -->
 * <!-- endchart -->
 * <!-- desc -->
 * <!-- enddesc -->
 * {% endchartjs %}
 */

'use strict'

const { escapeHTML } = require('hexo-util')

const chartjs = (args, content) => {
  if (!content) return

  const chartRegex = /<!--\s*chart\s*-->\n([\w\W\s\S]*?)<!--\s*endchart\s*-->/
  const descRegex = /<!--\s*desc\s*-->\n([\w\W\s\S]*?)<!--\s*enddesc\s*-->/
  const selfConfig = args.join(' ').trim()

  const [width = '', layout = false, chartId = ''] = selfConfig.split(',').map(s => s.trim())

  const chartMatch = content.match(chartRegex)
  const descMatch = content.match(descRegex)

  if (!chartMatch) {
    hexo.log.warn('chartjs tag: chart content is required!')
    return
  }

  const chartConfig = chartMatch && chartMatch[1] ? chartMatch[1] : ''
  const descContent = descMatch && descMatch[1] ? descMatch[1] : ''

  const renderedDesc = descContent ? hexo.render.renderSync({ text: descContent, engine: 'markdown' }).trim() : ''

  const descDOM = renderedDesc ? `<div class="chartjs-desc">${renderedDesc}</div>` : ''
  const abreastClass = layout ? ' chartjs-abreast' : ''
  const widthStyle = width ? `data-width="${width}%"` : ''

  return `<div class="chartjs-container${abreastClass}" data-chartjs-id="${chartId}" ${widthStyle}>
            <pre class="chartjs-src" hidden>${escapeHTML(chartConfig)}</pre>
            ${descDOM}
          </div>`
}

hexo.extend.tag.register('chartjs', chartjs, { ends: true })

```

### 文件路径: `themes\butterfly\scripts\tag\flink.js`
```js
/**
 * flink
 */

'use strict'

const urlFor = require('hexo-util').url_for.bind(hexo)

const flinkFn = (args, content) => {
  const data = hexo.render.renderSync({ text: content, engine: 'yaml' })
  let result = ''

  data.forEach(item => {
    const className = item.class_name ? `<div class="flink-name">${item.class_name}</div>` : ''
    const classDesc = item.class_desc ? `<div class="flink-desc">${item.class_desc}</div>` : ''

    const listResult = item.link_list.map(link => `
      <div class="flink-list-item">
        <a href="${link.link}" title="${link.name}" target="_blank">
          <div class="flink-item-icon">
            <img class="no-lightbox" src="${link.avatar}" onerror='this.onerror=null;this.src="${urlFor(hexo.theme.config.error_img.flink)}"' alt="${link.name}" />
          </div>
          <div class="flink-item-name">${link.name}</div>
          <div class="flink-item-desc" title="${link.descr}">${link.descr}</div>
        </a>
      </div>`).join('')

    result += `${className}${classDesc}<div class="flink-list">${listResult}</div>`
  })

  return `<div class="flink">${result}</div>`
}

hexo.extend.tag.register('flink', flinkFn, { ends: true })

```

### 文件路径: `themes\butterfly\scripts\tag\gallery.js`
```js
/**
 * Butterfly
 * galleryGroup and gallery
 * {% galleryGroup [name] [descr] [url] [img] %}
 *
 * {% gallery [button],[limit],[firstLimit] %}
 * {% gallery url,[url],[button] %}
 */

'use strict'

const urlFor = require('hexo-util').url_for.bind(hexo)

const DEFAULT_LIMIT = 10
const DEFAULT_FIRST_LIMIT = 10
const IMAGE_REGEX = /!\[(.*?)\]\(([^\s]*)\s*(?:["'](.*?)["']?)?\s*\)/g

// Helper functions
const parseGalleryArgs = args => {
  const [type, ...rest] = args.join(' ').split(',').map(arg => arg.trim())
  return {
    isUrl: type === 'url',
    params: type === 'url' ? rest : [type, ...rest]
  }
}

const parseImageContent = content => {
  const images = []
  let match

  while ((match = IMAGE_REGEX.exec(content)) !== null) {
    images.push({
      url: match[2],
      alt: match[1] || '',
      title: match[3] || ''
    })
  }

  return images
}

const createGalleryHTML = (type, dataStr, button, limit, firstLimit) => {
  return `<div class="gallery-container" data-type="${type}" data-button="${button}" data-limit="${limit}" data-first="${firstLimit}">
    <div class="gallery-items">${dataStr}</div>
  </div>`
}

const gallery = (args, content) => {
  const { isUrl, params } = parseGalleryArgs(args)

  if (isUrl) {
    const [dataStr, button = false, limit = DEFAULT_LIMIT, firstLimit = DEFAULT_FIRST_LIMIT] = params
    return createGalleryHTML('url', urlFor(dataStr), button, limit, firstLimit)
  }

  const [button = false, limit = DEFAULT_LIMIT, firstLimit = DEFAULT_FIRST_LIMIT] = params
  const images = parseImageContent(content)
  return createGalleryHTML('data', JSON.stringify(images), button, limit, firstLimit)
}

const galleryGroup = args => {
  const [name = '', descr = '', url = '', img = ''] = args.map(arg => arg.trim())

  return `<figure class="gallery-group">
    <img class="gallery-group-img no-lightbox" src='${urlFor(img)}' alt="Group Image Gallery">
    <figcaption>
      <div class="gallery-group-name">${name}</div>
      <p>${descr}</p>
      <a href='${urlFor(url)}'></a>
    </figcaption>
  </figure>`
}

// Register tags
hexo.extend.tag.register('gallery', gallery, { ends: true })
hexo.extend.tag.register('galleryGroup', galleryGroup)

```

### 文件路径: `themes\butterfly\scripts\tag\hide.js`
```js
/**
 * Butterfly
 * @example
 * hideInline
 * {% hideInline content,display,bg,color %}
 * content不能包含當引號，可用 &apos;
 * hideBlock
 * {% hideBlock display,bg,color %}
 * content
 * {% endhideBlock %}
 * hideToggle
 * {% hideToggle display,bg,color %}
 * content
 * {% endhideToggle %}
 */

'use strict'

const parseArgs = args => args.join(' ').split(',')

const generateStyle = (bg, color) => {
  let style = 'style="'
  if (bg) style += `background-color: ${bg};`
  if (color) style += `color: ${color}`
  style += '"'
  return style
}

const hideInline = args => {
  const [content, display = 'Click', bg = false, color = false] = parseArgs(args)
  const style = generateStyle(bg, color)
  return `<span class="hide-inline"><button type="button" class="hide-button" ${style}>${display}</button><span class="hide-content">${content}</span></span>`
}

const hideBlock = (args, content) => {
  const [display = 'Click', bg = false, color = false] = parseArgs(args)
  const style = generateStyle(bg, color)
  const renderedContent = hexo.render.renderSync({ text: content, engine: 'markdown' })
  return `<div class="hide-block"><button type="button" class="hide-button" ${style}>${display}</button><div class="hide-content">${renderedContent}</div></div>`
}

const hideToggle = (args, content) => {
  const [display, bg = false, color = false] = parseArgs(args)
  const style = generateStyle(bg, color)
  const border = bg ? `style="border: 1px solid ${bg}"` : ''
  const renderedContent = hexo.render.renderSync({ text: content, engine: 'markdown' })
  return `<details class="toggle" ${border}><summary class="toggle-button" ${style}>${display}</summary><div class="toggle-content">${renderedContent}</div></details>`
}

hexo.extend.tag.register('hideInline', hideInline)
hexo.extend.tag.register('hideBlock', hideBlock, { ends: true })
hexo.extend.tag.register('hideToggle', hideToggle, { ends: true })
```

### 文件路径: `themes\butterfly\scripts\tag\inlineImg.js`
```js
/**
 * inlineImg
 * @param {Array} args - Image name and height
 * @param {string} args[0] - Image name
 * @param {number} args[1] - Image height
 * @returns {string} - Image tag
 */

'use strict'

const urlFor = require('hexo-util').url_for.bind(hexo)

const inlineImg = ([img, height = '']) => {
  const heightStyle = height ? `style="height:${height}"` : ''
  const src = urlFor(img)
  return `<img class="inline-img" src="${src}" ${heightStyle} />`
}

hexo.extend.tag.register('inlineImg', inlineImg, { ends: false })

```

### 文件路径: `themes\butterfly\scripts\tag\label.js`
```js
/**
 * Butterfly
 * label
 * {% label text color %}
 */

'use strict'

const addLabel = args => {
  const [text, className = 'default'] = args
  return `<mark class="hl-label ${className}">${text}</mark>`
}

hexo.extend.tag.register('label', addLabel, { ends: false })

```

### 文件路径: `themes\butterfly\scripts\tag\mermaid.js`
```js
/**
 * Butterfly
 * mermaid
 * https://github.com/mermaid-js/mermaid
 */

'use strict'

const { escapeHTML } = require('hexo-util')

const mermaid = (args, content) => {
  return `<div class="mermaid-wrap"><pre class="mermaid-src" hidden>
    ${escapeHTML(content)}
  </pre></div>`
}

hexo.extend.tag.register('mermaid', mermaid, { ends: true })

```

### 文件路径: `themes\butterfly\scripts\tag\note.js`
```js
/**
 * note.js
 * transplant from hexo-theme-next
 * Modify by Jerry
 */

'use strict'

const postNote = (args, content) => {
  const styleConfig = hexo.theme.config.note.style
  const noteTag = ['flat', 'modern', 'simple', 'disabled']
  if (!noteTag.includes(args[args.length - 1])) {
    args.push(styleConfig)
  }

  let icon = ''
  const iconArray = args[args.length - 2]
  if (iconArray && iconArray.startsWith('fa')) {
    icon = `<i class="note-icon ${iconArray}"></i>`
    args[args.length - 2] = 'icon-padding'
  }

  return `<div class="note ${args.join(' ')}">${icon + hexo.render.renderSync({ text: content, engine: 'markdown' })}</div>`
}

hexo.extend.tag.register('note', postNote, { ends: true })
hexo.extend.tag.register('subnote', postNote, { ends: true })

```

### 文件路径: `themes\butterfly\scripts\tag\score.js`
```js
/**
 * Music Score
 * {% score %}
 */

'use strict'

const score = (args, content) => {
  const escapeHtmlTags = s => {
    const lookup = {
      '&': '&amp;',
      '"': '&quot;',
      '\'': '&apos;',
      '<': '&lt;',
      '>': '&gt;'
    }
    return s.replace(/[&"'<>]/g, c => lookup[c])
  }
  return `<div class="abc-music-sheet">${escapeHtmlTags(content)}</div>`
}

hexo.extend.tag.register('score', score, { ends: true })

```

### 文件路径: `themes\butterfly\scripts\tag\series.js`
```js
/**
 * series plugin
 * Syntax:
 *  {% series [series name] %}
 * Usage:
 * {% series %}
 * {% series series1 %}
 */

'use strict'

const urlFor = require('hexo-util').url_for.bind(hexo)
const groups = {}

hexo.extend.filter.register('before_post_render', data => {
  if (!hexo.theme.config.series.enable) return data

  const { layout, series } = data
  if (layout === 'post' && series) {
    if (!groups[series]) groups[series] = []
    groups[series].push({
      title: data.title,
      path: data.path,
      date: data.date.unix()
    })
  }
  return data
})

function series (args) {
  const { series } = hexo.theme.config
  if (!series.enable) {
    hexo.log.warn('Series plugin is disabled in the theme config')
    return ''
  }

  const seriesArr = args.length ? groups[args[0]] : groups[this.series]

  if (!seriesArr) {
    hexo.log.warn(`There is no series named "${args[0]}"`)
    return ''
  }

  const isAsc = (series.order || 1) === 1 // 1: asc, -1: desc
  const isSortByTitle = series.orderBy === 'title'

  const compareFn = (a, b) => {
    const itemA = isSortByTitle ? a.title.toUpperCase() : a.date
    const itemB = isSortByTitle ? b.title.toUpperCase() : b.date

    return itemA < itemB ? (isAsc ? -1 : 1) : itemA > itemB ? (isAsc ? 1 : -1) : 0
  }

  seriesArr.sort(compareFn)

  const listItems = seriesArr.map(ele =>
    `<li><a href="${urlFor(ele.path)}" title="${ele.title}">${ele.title}</a></li>`
  ).join('')

  return series.number ? `<ol class="series-items">${listItems}</ol>` : `<ul class="series-items">${listItems}</ul>`
}

hexo.extend.tag.register('series', series, { ends: false })

```

### 文件路径: `themes\butterfly\scripts\tag\tabs.js`
```js
/**
 * Tabs
 * transplant from hexo-theme-next
 * modify by Jerry
 */

'use strict'

const postTabs = (args, content) => {
  const tabBlock = /<!--\s*tab (.*?)\s*-->\n([\w\W\s\S]*?)<!--\s*endtab\s*-->/g
  args = args.join(' ').split(',')
  const tabName = args[0] || 'tab'
  const tabActive = Number(args[1]) || 0
  const matches = []
  let match
  let tabId = 0
  let tabNav = ''
  let tabContent = ''
  let noDefault = true

  while ((match = tabBlock.exec(content)) !== null) {
    matches.push(match[1], match[2])
  }

  for (let i = 0; i < matches.length; i += 2) {
    const [tabCaption = '', tabIcon = ''] = matches[i].split('@')
    let postContent = matches[i + 1]

    postContent = hexo.render.renderSync({ text: postContent, engine: 'markdown' }).trim()
    tabId += 1

    const caption = (tabCaption || tabIcon) ? tabCaption : `${tabName} ${tabId}`
    const iconHtml = tabIcon ? `<i class="${tabIcon.trim()}"></i>` : ''
    const isActive = (tabActive > 0 && tabActive === tabId) || (tabActive === 0 && tabId === 1) ? ' active' : ''

    if (isActive) noDefault = false

    tabNav += `<button type="button" class="tab${isActive}">${iconHtml}${caption.trim()}</button>`
    tabContent += `<div class="tab-item-content${isActive}">${postContent}</div>`
  }

  const toTop = '<div class="tab-to-top"><button type="button" aria-label="scroll to top"><i class="fas fa-arrow-up"></i></button></div>'
  tabNav = `<div class="nav-tabs${noDefault ? ' no-default' : ''}">${tabNav}</div>`
  tabContent = `<div class="tab-contents">${tabContent}</div>`

  return `<div class="tabs">${tabNav}${tabContent}${toTop}</div>`
}

hexo.extend.tag.register('tabs', postTabs, { ends: true })
hexo.extend.tag.register('subtabs', postTabs, { ends: true })
hexo.extend.tag.register('subsubtabs', postTabs, { ends: true })

```

### 文件路径: `themes\butterfly\scripts\tag\timeline.js`
```js
/**
 * Timeline tag for Hexo
 * Syntax:
 * {% timeline [headline],[color] %}
 * <!-- timeline [title] -->
 * [content]
 * <!-- endtimeline -->
 * <!-- timeline [title] -->
 * [content]
 * <!-- endtimeline -->
 * {% endtimeline %}
 */

'use strict'

const timeLineFn = (args, content) => {
  // Use named capture groups for better readability
  const tlBlock = /<!--\s*timeline\s*(?<title>.*?)\s*-->\n(?<content>[\s\S]*?)<!--\s*endtimeline\s*-->/g

  // Pre-compile markdown render function
  const renderMd = text => hexo.render.renderSync({ text, engine: 'markdown' })

  // Parse arguments more efficiently
  const [text, color = ''] = args.length ? args.join(' ').split(',') : []

  // Build initial headline if text exists
  const headline = text
    ? `<div class='timeline-item headline'>
        <div class='timeline-item-title'>
          <div class='item-circle'>${renderMd(text)}</div>
        </div>
      </div>`
    : ''

  // Match all timeline blocks in one pass and transform
  const items = Array.from(content.matchAll(tlBlock))
    .map(({ groups: { title, content } }) =>
      `<div class='timeline-item'>
        <div class='timeline-item-title'>
          <div class='item-circle'>${renderMd(title)}</div>
        </div>
        <div class='timeline-item-content'>${renderMd(content)}</div>
      </div>`
    )
    .join('')

  return `<div class="timeline ${color}">${headline}${items}</div>`
}

hexo.extend.tag.register('timeline', timeLineFn, { ends: true })

```

### 文件路径: `themes\butterfly\source\css\index.styl`
```styl
if hexo-config('css_prefix')
  @import 'nib'

@import '_third-party/normalize.min.css'
// project
@import 'var'
@import '_global/*'
@import '_highlight/highlight'
@import '_page/*'
@import '_layout/*'
@import '_tags/*'
@import '_mode/*'

// search
@import '_search/index'
```

### 文件路径: `themes\butterfly\source\css\var.styl`
```styl
// color
$bright-blue = #49B1F5
$strong-cyan = #00c4b6
$light-orange = #FF7242
$light-red = #F47466
$themeColorEnable = hexo-config('theme_color') && hexo-config('theme_color.enable')
$theme-color = $themeColorEnable && hexo-config('theme_color.main') ? convert(hexo-config('theme_color.main')) : $bright-blue
$theme-paginator-color = $themeColorEnable && hexo-config('theme_color.paginator') ? convert(hexo-config('theme_color.paginator')) : $strong-cyan
$theme-text-selection-color = $themeColorEnable && hexo-config('theme_color.text_selection') ? convert(hexo-config('theme_color.text_selection')) : $strong-cyan
$theme-link-color = $themeColorEnable && hexo-config('theme_color.link_color') ? convert(hexo-config('theme_color.link_color')) : $bright-blue
$theme-hr-color = $themeColorEnable && hexo-config('theme_color.hr_color') ? convert(hexo-config('theme_color.hr_color')) : $bright-blue
$code-foreground = $themeColorEnable && hexo-config('theme_color.code_foreground') ? convert(hexo-config('theme_color.code_foreground')) : $light-red
$code-background = $themeColorEnable && hexo-config('theme_color.code_background') ? convert(hexo-config('theme_color.code_background')) : rgba(27, 31, 35, .05)
$theme-toc-color = $themeColorEnable && hexo-config('theme_color.toc_color') ? convert(hexo-config('theme_color.toc_color')) : $strong-cyan
// font

$chinseFont = $language == 'zh-CN' ? 'Microsoft YaHei' : 'Microsoft JhengHei'
$dafault-font-family = -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Lato, Roboto, 'PingFang SC', $chinseFont, sans-serif
$dafault-code-font = consolas, Menlo, monospace, 'PingFang SC', $chinseFont, sans-serif

$font-family = hexo-config('font.font_family') ? unquote(hexo-config('font.font_family')) : $dafault-font-family
$code-font-family = hexo-config('font.code_font_family') ? unquote(hexo-config('font.code_font_family')) : $dafault-code-font
$site-name-font = hexo-config('blog_title_font.font_family') && unquote(hexo-config('blog_title_font.font_family'))
// hr
$hrEnable = hexo-config('hr_icon') && hexo-config('hr_icon.enable')
$hr-icon = $hrEnable && hexo-config('hr_icon.icon') ? hexo-config('hr_icon.icon') : '\f0c4'
$hr-icon-top = $hrEnable && hexo-config('hr_icon.icon_top') ? convert(hexo-config('hr_icon.icon_top')) : -10px
// page beatutify
$beautifyEnable = hexo-config('beautify.enable')
$title-prefix-icon = $beautifyEnable && hexo-config('beautify.title_prefix_icon') ? hexo-config('beautify.title_prefix_icon') : '\f0c1'
$title-prefix-icon-color = $beautifyEnable && hexo-config('beautify.title_prefix_icon_color') ? convert(hexo-config('beautify.title_prefix_icon_color')) : $light-red
// Global Variables
$font-size = hexo-config('font.global_font_size') ? convert(hexo-config('font.global_font_size')) : 14px
$code-font-size = hexo-config('font.code_font_size') ? convert(hexo-config('font.code_font_size')) : var(--global-font-size)
$font-color = #1F2D3D
$text-line-height = 2
$index_top_img_height = hexo-config('index_top_img_height') ? convert(hexo-config('index_top_img_height')) : 100vh
$index_site_info_top = hexo-config('index_site_info_top') ? convert(hexo-config('index_site_info_top')) : 43%
// Global color & SVG
$light-blue = $theme-color
$dark-black = #000000
$light-grey = #EEEEEE
$grey = #858585
$dark-grey = #cacaca
$white = #FFFFFF
$whitesmoke = #f5f5f5
$font-black = #4C4948
$card-bg = $white
$text-highlight-color = $font-color
$text-hover = $theme-color
$text-bg-hover = $theme-color
// code
$line-height-code-block = 1.6
$blockquote-color = #6a737d
$blockquote-padding-color = $themeColorEnable && hexo-config('theme_color.blockquote_padding_color') ? convert(hexo-config('theme_color.blockquote_padding_color')) : #49B1F5
$blockquote-background-color = $themeColorEnable && hexo-config('theme_color.blockquote_background_color') ? alpha(convert(hexo-config('theme_color.blockquote_background_color')), .1) : alpha($blockquote-padding-color, .1)
// page
$body-bg = #fff
$a-link-color = #99a9bf
$sticky-color = $light-orange
$theme-meta-color = $themeColorEnable && hexo-config('theme_color.meta_color') ? convert(hexo-config('theme_color.meta_color')) : #858585
// sidebar
$sidebar-background = #f6f8fa
$sidebar-width = 330px
// aside
$toc-link-color = #666261
$toc-mobile-width = calc(100% - 80px)
$toc-mobile-maxWidth = 380px
$toc-active-color = #fff
// Button
$button-color = #fff
$button-hover-color = $themeColorEnable && hexo-config('theme_color.button_hover') ? convert(hexo-config('theme_color.button_hover')) : $light-orange
$button-bg = $theme-color
$pseudo-hover = $button-hover-color
// scrollbar
$scrollbar-color = $themeColorEnable && hexo-config('theme_color.scrollbar_color') ? convert(hexo-config('theme_color.scrollbar_color')) : $theme-color
// table
$table-thead-bg = #99a9bf
// reward
$reward-pop-up-bg = #f5f5f5
$reward-pop-up-color = #858585
// search
$search-bg = #f6f8fa
$search-input-color = $font-black
$search-color = $theme-color
$search-keyword-highlight = #F47466
$search-a-color = $font-black
// comments
$comments-switch-first-text = $bright-blue
$comments-switch-second-text = $light-orange
$comments-switch-round = #fff
$comments-switch-bg = #f6f8fa
// noticeOutdate
$noticeOutdate-bg = #ffe6e6
$noticeOutdate-color = #ff6666
$noticeOutdate-border = #ff8080
// gallery
$gallery-color = #fff
// tag-hide
$tag-hide-bg = $theme-color
$tag-hide-toggle-bg = #f0f0f0
// preloader
$preloader-bg = #37474f
$preloader-word-color = #fff
// rightside
$rightside-bottom = hexo-config('rightside_bottom') ? convert(hexo-config('rightside_bottom')) : 40px
// fireworks
$fireworks-zIndex = hexo-config('fireworks.zIndex') ? hexo-config('fireworks.zIndex') : 99999
// Tag Plugins - Note
hexo-config('note.light_bg_offset') is a 'unit' ? ($lbg = unit(hexo-config('note.light_bg_offset'), '%')) : ($lbg = 0)
$note-types = 'default' 'primary' 'info' 'success' 'warning' 'danger'
// Default
$note-default-border = #777
$note-default-bg = lighten(spin($note-default-border, 0), 94% + $lbg)
$note-default-text = $note-default-border
$note-default-icon = '\f0a9'
$note-modern-default-border = #e1e1e1
$note-modern-default-bg = lighten(spin($note-modern-default-border, 10), 60% + ($lbg * 4))
$note-modern-default-text = #666
$note-modern-default-hover = darken(spin($note-modern-default-text, -10), 32%)
// Primary
$note-primary-border = #6f42c1
$note-primary-bg = lighten(spin($note-primary-border, 10), 92% + $lbg)
$note-primary-text = $note-primary-border
$note-primary-icon = '\f055'
$note-modern-primary-border = #e1c2ff
$note-modern-primary-bg = lighten(spin($note-modern-primary-border, 10), 40% + ($lbg * 4))
$note-modern-primary-text = #6f42c1
$note-modern-primary-hover = darken(spin($note-modern-primary-text, -10), 22%)
// Info
$note-info-border = #428bca
$note-info-bg = lighten(spin($note-info-border, -10), 91% + $lbg)
$note-info-text = $note-info-border
$note-info-icon = '\f05a'
$note-modern-info-border = #b3e5ef
$note-modern-info-bg = lighten(spin($note-modern-info-border, 10), 50% + ($lbg * 4))
$note-modern-info-text = #31708f
$note-modern-info-hover = darken(spin($note-modern-info-text, -10), 32%)
// Success
$note-success-border = #5cb85c
$note-success-bg = lighten(spin($note-success-border, 10), 90% + $lbg)
$note-success-text = $note-success-border
$note-success-icon = '\f058'
$note-modern-success-border = #d0e6be
$note-modern-success-bg = lighten(spin($note-modern-success-border, 10), 40% + ($lbg * 4))
$note-modern-success-text = #3c763d
$note-modern-success-hover = darken(spin($note-modern-success-text, -10), 27%)
// Warning
$note-warning-border = #f0ad4e
$note-warning-bg = lighten(spin($note-warning-border, 10), 88% + $lbg)
$note-warning-text = $note-warning-border
$note-warning-icon = '\f06a'
$note-modern-warning-border = #fae4cd
$note-modern-warning-bg = lighten(spin($note-modern-warning-border, 10), 43% + ($lbg * 4))
$note-modern-warning-text = #8a6d3b
$note-modern-warning-hover = darken(spin($note-modern-warning-text, -10), 18%)
// Danger
$note-danger-border = #d9534f
$note-danger-bg = lighten(spin($note-danger-border, -10), 92% + $lbg)
$note-danger-text = $note-danger-border
$note-danger-icon = '\f056'
$note-modern-danger-border = #ebcdd2
$note-modern-danger-bg = lighten(spin($note-modern-danger-border, 10), 35% + ($lbg * 4))
$note-modern-danger-text = #a94442
$note-modern-danger-hover = darken(spin($note-modern-danger-text, -10), 22%)
// Tag Plugins - Button/note
$color-types = 'blue' 'pink' 'red' 'purple' 'orange' 'green'
$btn-color = #fff
$btn-default-color = #777
$tagsP-blue-color = #428bca
$tagsP-pink-color = #FF69B4
$tagsP-red-color = #FF0000
$tagsP-orange-color = #FF8C00
$tagsP-purple-color = #6f42c1
$tagsP-green-color = #5cb85c
// Tag Plugins - Tab
$tab-border-color = #f0f0f0
$tab-botton-bg = #f0f0f0
$tab-botton-color = $font-color
$tab-button-hover-bg = darken($tab-border-color, 8)
$tab-active-border-color = $theme-color
$tab-button-active-bg = $card-bg
$tab-to-top-color = #99a9bf
$tab-to-top-hover-color = $theme-color
// Tag Plugins - timeline
$timeline-default-color = $theme-color

```

### 文件路径: `themes\butterfly\source\css\_global\function.styl`
```styl
.limit-one-line
  overflow: hidden
  text-overflow: ellipsis
  white-space: nowrap

.limit-more-line
  display: -webkit-box
  overflow: hidden
  -webkit-box-orient: vertical

.fontawesomeIcon
  display: inline-block
  font-weight: 600
  font-family: 'Font Awesome 6 Free'
  text-rendering: auto
  -webkit-font-smoothing: antialiased

addBorderRadius(x = 6, hide = false)
  if hexo-config('rounded_corners_ui')
    border-radius: unit(x, 'px')

    if hide
      overflow: hidden

// card hover
.cardHover
  background: var(--card-bg)
  box-shadow: var(--card-box-shadow)
  transition: all .3s
  addBorderRadius(8)

  &:hover
    box-shadow: var(--card-hover-box-shadow)

.imgHover
  width: 100%
  height: 100%
  transition: filter 375ms ease-in .2s, transform .6s
  object-fit: cover

  &:hover
    transform: scale(1.1)

.postImgHover
  &:hover
    .cover
      opacity: .5
      transform: scale(1.1)

  .cover
    width: 100%
    height: 100%
    opacity: .4
    transition: all .6s, filter 375ms ease-in .2s
    object-fit: cover

.list-beauty
  list-style: none

  li
    position: relative
    padding: .12em .4em .12em 1.4em

    &:hover
      &:before
        border-color: var(--pseudo-hover)

    &:before
      position: absolute
      top: .67em
      left: 0
      width: w = .43em
      height: h = w
      border: .5 * w solid $light-blue
      border-radius: w
      background: transparent
      content: ''
      cursor: pointer
      transition: all .3s ease-out

.custom-hr
  position: relative
  margin: 40px auto
  border: 2px dashed var(--hr-border)

  if hexo-config('hr_icon.enable')
    width: calc(100% - 4px)

    &:hover
      &:before
        left: calc(95% - 20px)

    &:before
      position: absolute
      top: $hr-icon-top
      left: 5%
      z-index: 1
      color: var(--hr-before-color)
      content: $hr-icon
      font-size: 20px
      line-height: 1
      transition: all 1s ease-in-out
      @extend .fontawesomeIcon

.verticalCenter
  position: absolute
  top: 50%
  width: 100%
  transform: translate(0, -50%)

maxWidth600()
  @media screen and (max-width: 600px)
    {block}

maxWidth768()
  @media screen and (max-width: 768px)
    {block}

minWidth768()
  @media screen and (min-width: 768px)
    {block}

maxWidth1024()
  @media screen and (max-width: 1024px)
    {block}

minWidth1024()
  @media screen and (min-width: 1024px)
    {block}

maxWidth900()
  @media screen and (max-width: 900px)
    {block}

minWidth901()
  @media screen and (min-width: 901px)
    {block}

minWidth900()
  @media screen and (min-width: 900px)
    {block}

minWidth2000()
  @media screen and (min-width: 2000px)
    {block}

// animation
if hexo-config('enter_transitions')
  #content-inner,
  #footer
    animation: bottom-top 1s

  #page-header:not(.full_page),
  #nav.show
    animation: header-effect 1s

  #site-title,
  #site-subtitle
    animation: titleScale 1s

  canvas:not(#ribbon-canvas),
  #web_bg
    animation: to_show 4s

  #ribbon-canvas
    animation: ribbon_to_show 4s

  #sidebar-menus
    &.open
      for i in 1 2 3 4
        > :nth-child({i})
          animation: sidebarItem (i / 5s)

.scroll-down-effects
  animation: scroll-down-effect 1.5s infinite

if hexo-config('avatar.effect') == true
  .avatar-img
    animation: avatar_turn_around 2s linear infinite

.reward-main
  animation: donate_effcet .3s .1s ease both

@keyframes scroll-down-effect
  0%
    opacity: .4
    transform: translate(0, 0)

  50%
    opacity: 1
    transform: translate(0, -16px)

  100%
    opacity: .4
    transform: translate(0, 0)

@keyframes header-effect
  0%
    transform: translateY(-35px)

  100%
    transform: translateY(0)

@keyframes bottom-top
  0%
    transform: translateY(35px)

  100%
    transform: translateY(0)

@keyframes titleScale
  0%
    opacity: 0
    transform: scale(.7)

  100%
    opacity: 1
    transform: scale(1)

@keyframes search_close
  0%
    opacity: 1
    transform: scale(1)

  100%
    opacity: 0
    transform: scale(.7)

@keyframes to_show
  0%
    opacity: 0

  100%
    opacity: 1

@keyframes to_hide
  0%
    opacity: 1

  100%
    opacity: 0

@keyframes ribbon_to_show
  0%
    opacity: 0

  100%
    opacity: hexo-config('canvas_ribbon.alpha')

@keyframes avatar_turn_around
  from
    transform: rotate(0)

  to
    transform: rotate(360deg)

@keyframes sub_menus
  0%
    opacity: 0
    transform: translateY(10px)

  100%
    opacity: 1
    transform: translateY(0)

@keyframes donate_effcet
  0%
    opacity: 0
    transform: translateY(-20px)

  100%
    opacity: 1
    transform: translateY(0)

@keyframes sidebarItem
  0%
    transform: translateX(200px)

  100%
    transform: translateX(0)

```

### 文件路径: `themes\butterfly\source\css\_global\index.styl`
```styl
:root
  --global-font-size: $font-size
  --global-bg: $body-bg
  --font-color: $font-black
  --hr-border: lighten($theme-hr-color, 50%)
  --hr-before-color: lighten($theme-hr-color, 30%)
  --search-bg: $search-bg
  --search-input-color: $search-input-color
  --search-a-color: $search-a-color
  --preloader-bg: $preloader-bg
  --preloader-color: $preloader-word-color
  --tab-border-color: $tab-border-color
  --tab-botton-bg: $tab-botton-bg
  --tab-botton-color: $tab-botton-color
  --tab-button-hover-bg: $tab-button-hover-bg
  --tab-button-active-bg: $tab-button-active-bg
  --card-bg: $card-bg
  --card-meta: $theme-meta-color
  --sidebar-bg: $sidebar-background
  --sidebar-menu-bg: $white
  --btn-hover-color: $button-hover-color
  --btn-color: $button-color
  --btn-bg: $button-bg
  --text-bg-hover: rgba($text-bg-hover, .7)
  --light-grey: $light-grey
  --dark-grey: $dark-grey
  --white: $white
  --text-highlight-color: $text-highlight-color
  --blockquote-color: $blockquote-color
  --blockquote-bg: $blockquote-background-color
  --reward-pop: $reward-pop-up-bg
  --toc-link-color: $toc-link-color
  --card-box-shadow: 0 3px 8px 6px rgba(7, 17, 27, .05)
  --card-hover-box-shadow: 0 3px 8px 6px rgba(7, 17, 27, .09)
  --pseudo-hover: $pseudo-hover
  --headline-presudo: #a0a0a0
  --scrollbar-color: $scrollbar-color
  --default-bg-color: $theme-color
  --zoom-bg: #fff
  --mark-bg: alpha($dark-black, .3)

body
  position: relative
  overflow-y: scroll
  min-height: 100%
  background: var(--global-bg)
  color: var(--font-color)
  font-size: var(--global-font-size)
  font-family: $font-family
  line-height: $text-line-height
  -webkit-tap-highlight-color: rgba(0, 0, 0, 0)
  scroll-behavior: smooth

  if !hexo-config('copy.enable')
    user-select: none
    -webkit-user-select: none

// scrollbar - firefox
@-moz-document url-prefix()
  *
    scrollbar-width: thin
    scrollbar-color: var(--scrollbar-color) transparent

// scrollbar - chrome/safari
*::-webkit-scrollbar
  width: 5px
  height: 5px

*::-webkit-scrollbar-thumb
  background: var(--scrollbar-color)

*::-webkit-scrollbar-track
  background-color: transparent

input::placeholder
  color: var(--font-color)

if hexo-config('background')
  #web_bg
    position: fixed
    z-index: -999
    width: 100%
    height: 100%
    background-attachment: local
    background-position: center
    background-size: cover
    background-repeat: no-repeat

h1,
h2,
h3,
h4,
h5,
h6
  position: relative
  margin: 20px 0 14px
  color: var(--text-highlight-color)
  font-weight: bold

  code
    font-size: inherit !important

*
  box-sizing: border-box

.table-wrap
  overflow-x: scroll
  margin: 0 0 20px

  if hexo-config('rounded_corners_ui')
    $borderRadius = 5px
    border-radius: $borderRadius

    table
      border-radius: $borderRadius

      thead > tr:first-child
        th:first-child
          border-top-left-radius: $borderRadius

        th:last-child
          border-top-right-radius: $borderRadius

      tbody > tr:last-child
        td:first-child
          border-bottom-left-radius: $borderRadius

        td:last-child
          border-bottom-right-radius: $borderRadius

table
  display: table
  width: 100%
  border-spacing: 0
  border-collapse: separate
  border-top: 1px solid var(--light-grey)
  border-left: 1px solid var(--light-grey)
  empty-cells: show

  thead
    background: alpha($table-thead-bg, 10%)

  th,
  td
    padding: 6px 12px
    border: 1px solid var(--light-grey)
    border-top: none
    border-left: none
    vertical-align: middle

*::selection
  background: $theme-text-selection-color
  color: #F7F7F7

button
  padding: 0
  outline: 0
  border: none
  background: none
  cursor: pointer
  touch-action: manipulation

a
  color: $a-link-color
  text-decoration: none
  word-wrap: break-word
  transition: all .2s
  overflow-wrap: break-word

  &:hover
    color: $light-blue

// font
if $site-name-font
  #site-title,
  #site-subtitle,
  .site-name,
  #aside-content .author-info-name,
  #aside-content .author-info-description
    font-family: $site-name-font

.text-center
  text-align: center

.text-right
  text-align: right

img
  &[src=''],
  &:not([src])
    opacity: 0

// lazyload blur
if hexo-config('lazyload.enable') && hexo-config('lazyload.blur') && !hexo-config('lazyload.placeholder')
  img
    &[data-lazy-src]:not(.loaded)
      filter: blur(8px) brightness(1)

    &[data-lazy-src].error
      filter: none

.img-alt
  margin: -10px 0 10px
  color: #858585

  &:hover
    text-decoration: none !important

blockquote
  margin: 0 0 20px
  padding: 7px 15px
  border-left: 4px solid $blockquote-padding-color
  background-color: var(--blockquote-bg)
  color: var(--blockquote-color)
  addBorderRadius()

  footer
    cite
      &:before
        padding: 0 5px
        content: '—'

  & > :last-child
    margin-bottom: 0 !important

```

### 文件路径: `themes\butterfly\source\css\_highlight\highlight.styl`
```styl
$highlight_theme = hexo-config('code_blocks.theme')
$highlight_macstyle = hexo-config('code_blocks.macStyle')
wordWrap = $highlight_enable && !$highlight_line_number && hexo-config('code_blocks.word_wrap')

@require 'theme'

:root
  --hl-color: $highlight-foreground
  --hl-bg: $highlight-background
  --hltools-bg: $highlight-tools.bg-color
  --hltools-color: $highlight-tools.color
  --hlnumber-bg: $highlight-gutter.bg-color
  --hlnumber-color: $highlight-gutter.color
  --hlscrollbar-bg: $highlight-scrollbar
  --hlexpand-bg: linear-gradient(180deg, rgba($highlight-background, .6), rgba($highlight-background, .9))

[data-theme='dark']
  --hl-color: alpha(#FFFFFF, .7)
  --hl-bg: lighten(#121212, 2)
  --hltools-bg: lighten(#121212, 3)
  --hltools-color: #90a4ae
  --hlnumber-bg: lighten(#121212, 2)
  --hlnumber-color: alpha(#FFFFFF, .4)
  --hlscrollbar-bg: lighten(#121212, 5)
  --hlexpand-bg: linear-gradient(180deg, rgba(lighten(#121212, 2), .6), rgba(lighten(#121212, 2), .9))

if $highlight_enable
  @require 'highlight/index'

if $prismjs_enable
  @require 'prismjs/index'

$code-block
  overflow: auto
  margin: 0 0 20px
  padding: 0
  background: var(--hl-bg)
  color: var(--hl-color)
  line-height: $line-height-code-block

  if wordWrap
    counter-reset: line
    white-space: pre-wrap

.container
  pre,
  code
    font-size: $code-font-size
    font-family: $code-font-family !important
    addBorderRadius()

  code
    padding: 2px 5px
    background: $code-background
    color: $code-foreground

  pre
    @extend $code-block
    padding: 10px 20px

    code
      padding: 0
      background: none
      color: var(--hl-color)
      text-shadow: none

  figure.highlight
    @extend $code-block
    position: relative
    addBorderRadius()

    pre
      margin: 0
      padding: 8px 0
      border: none

    figcaption,
    .caption
      padding: 6px 0 2px 14px
      font-size: $code-font-size
      line-height: 1em

      a
        float: right
        padding-right: 10px
        color: var(--hl-color)

        &:hover
          border-bottom-color: var(--hl-color)

    &.copy-true
      user-select: all
      -webkit-user-select: all

      & > table,
      & > pre
        display: block !important
        opacity: 0

  .highlight-tools
    display: flex
    align-items: center
    padding: 0 8px
    min-height: 24px
    height: 2.15em
    background: var(--hltools-bg)
    color: var(--hltools-color)
    font-size: $code-font-size
    overflow: hidden

    & > *
      padding: 5px

    i
      cursor: pointer
      transition: all .3s

      &:hover
        color: $theme-color

    &.closed
      & ~ *
        display: none

      .expand
        transform: rotate(-90deg)

    if !$highlight_macstyle
      & > .macStyle
        padding: 0

    .code-lang
      flex: 1
      text-transform: uppercase
      font-weight: bold
      font-size: 1.15em
      user-select: none
      -webkit-user-select: none
      padding 2px

    .copy-notice
      padding-right: 2px
      opacity: 0
      transition: opacity .4s

    if hexo-config('code_blocks.language')
      .code-lang
        flex: 1
    else if (!$highlight_macstyle && hexo-config('code_blocks.shrink') != 'none')
      & > div:nth-child(2)
        flex: 1
    else
      .macStyle
        flex: 1

  .gutter
    user-select: none
    -webkit-user-select: none

  .gist table
    width: auto

    td
      border: none

if $highlight_macstyle
  .container
    figure.highlight
      margin: 0 0 24px
      border-radius: 7px
      box-shadow: 0 5px 10px 0 $highlight-mac-border
      -webkit-transform: translateZ(0)

      .highlight-tools
        .macStyle
          display: flex

          & > *
            margin-right: 8px
            width: 12px
            height: 12px
            border-radius: 50%

          & > :last-child
            margin-right: 5px

          .mac-close
            background: #fc625d

          .mac-minimize
            background: #fdbc40

          .mac-maximize
            background: #35cd4b

        if hexo-config('code_blocks.shrink') != 'none'
          & > :nth-child(2)
            order: 8

          &.closed
            .expand
              transform: rotate(90deg)

if hexo-config('code_blocks.height_limit')
  .container
    .code-expand-btn
      position: absolute
      bottom: 0
      z-index: 10
      width: 100%
      background: var(--hlexpand-bg)
      text-align: center
      font-size: $code-font-size
      cursor: pointer

      i
        padding: 6px 0
        color: var(--hlnumber-color)
        animation: code-expand-key 1.2s infinite

      &.expand-done
        & > i
          transform: rotate(180deg)

        & + table,
        & + pre
          margin-bottom: 1.8em

      &:not(.expand-done)
        & ~ table,
        & ~ pre
          overflow: hidden
          height: unit(hexo-config('code_blocks.height_limit'), px)
  
  @keyframes code-expand-key
    0%
      opacity: .6

    50%
      opacity: .1

    100%
      opacity: .6

if hexo-config('code_blocks.fullpage')
  .container
    figure.highlight.code-fullpage
      position: fixed
      top: 0
      right: 0
      bottom: 0
      left: 0
      z-index: 9999
      margin: 0
      border-radius: 0
      animation: code-fullpage .3s

      .code-expand-btn,
      .expand
        display: none

      .highlight-tools
        & ~ pre,
        & ~ table
          display: block
          overflow: auto
          height: calc(100vh - 2.15em)
          margin-bottom: 0

  @keyframes code-fullpage
    0%,
    100%
      transform: translateX(0)

    20%,
    60%
      transform: translateX(-5px)

    40%,
    80%
      transform: translateX(5px)
```

### 文件路径: `themes\butterfly\source\css\_highlight\theme.styl`
```styl
if $highlight_theme == 'darker'
  $highlight-background = #212121
  $highlight-selection = #61616150
  $highlight-foreground = #EEFFFF
  $highlight-mac-border = rgba(0, 0, 0, .4)
  $highlight-gutter = {
    color: alpha($highlight-foreground, .5),
    bg-color: $highlight-background
  }
  $highlight-tools = {
    color: alpha($highlight-foreground, .8),
    bg-color: darken($highlight-background, 2)
  }
  $highlight-scrollbar = lighten($highlight-background, 8)

  if $highlight_enable
    $highlight-comment = #969896
    $highlight-red = #FF5370
    $highlight-orange = #F78C6C
    $highlight-yellow = #FFCB6B
    $highlight-green = #C3E88D
    $highlight-aqua = #89DDFF
    $highlight-blue = #82AAFF
    $highlight-purple = #C792EA
    $highlight-deletion = #BF42BF
    $highlight-addition = #105EDE

if $highlight_theme == 'pale night'
  $highlight-background = #292D3E
  $highlight-selection = #717CB450
  $highlight-foreground = #A6ACCD
  $highlight-mac-border = rgba($highlight-background, .4)
  $highlight-gutter = {
    color: alpha($highlight-foreground, .5),
    bg-color: $highlight-background
  }
  $highlight-tools = {
    color: $highlight-foreground,
    bg-color: darken($highlight-background, 2)
  }
  $highlight-scrollbar = lighten($highlight-background, 8)

  if $highlight_enable
    $highlight-comment = #676E95
    $highlight-red = #FF5370
    $highlight-orange = #F78C6C
    $highlight-yellow = #FFCB6B
    $highlight-green = #C3E88D
    $highlight-aqua = #89DDFF
    $highlight-blue = #82AAFF
    $highlight-purple = #C792EA
    $highlight-deletion = #BF42BF
    $highlight-addition = #105EDE

if $highlight_theme == 'ocean'
  $highlight-background = #0F111A
  $highlight-selection = #717CB450
  $highlight-foreground = #8F93A2
  $highlight-mac-border = rgba($highlight-background, .4)
  $highlight-gutter = {
    color: alpha($highlight-foreground, .5),
    bg-color: $highlight-background
  }
  $highlight-tools = {
    color: $highlight-foreground,
    bg-color: darken($highlight-background, 2)
  }
  $highlight-scrollbar = lighten($highlight-background, 8)

  if $highlight_enable
    $highlight-comment = rgba(101, 115, 126, .8)
    $highlight-red = #FF5370
    $highlight-orange = #F78C6C
    $highlight-yellow = #FFCB6B
    $highlight-green = #C3E88D
    $highlight-aqua = #89DDFF
    $highlight-blue = #82AAFF
    $highlight-purple = #C792EA
    $highlight-deletion = #BF42BF
    $highlight-addition = #105EDE

if $highlight_theme == 'light'
  $highlight-background = #F6F8FA
  $highlight-selection = #80CBC440
  $highlight-foreground = #90A4AE
  $highlight-mac-border = rgba(144, 164, 174, .4)
  $highlight-tools = {
    color: $highlight-foreground,
    bg-color: darken($highlight-background, 5)
  }
  $highlight-gutter = {
    color: alpha($highlight-foreground, .5),
    bg-color: $highlight-background
  }
  $highlight-scrollbar = darken($highlight-background, 8)

  if $highlight_enable
    $highlight-comment = rgba(149, 165, 166, .8)
    $highlight-red = #E53935
    $highlight-orange = #F76D47
    $highlight-yellow = #FFB62C
    $highlight-green = #91B859
    $highlight-aqua = #39ADB5
    $highlight-blue = #6182B8
    $highlight-purple = #7C4DFF
    $highlight-deletion = #BF42BF
    $highlight-addition = #105EDE

if $highlight_theme == false
  $highlight-background = #F6F8FA
  $highlight-foreground = #90A4AE
  $highlight-selection = #80CBC440
  $highlight-gutter = {
    color: alpha($highlight-foreground, .5),
    bg-color: $highlight-background
  }
  $highlight-tools = {
    color: $highlight-foreground,
    bg-color: darken($highlight-background, 5)
  }
  $highlight-scrollbar = darken($highlight-background, 8)

```

### 文件路径: `themes\butterfly\source\css\_highlight\highlight\diff.styl`
```styl
figure.highlight
  table
    // scrollbar - firefox
    @-moz-document url-prefix()
      scrollbar-color: var(--hlscrollbar-bg) transparent

    &::-webkit-scrollbar-thumb
      background: var(--hlscrollbar-bg)

  pre .deletion
    color: $highlight-deletion

  pre .addition
    color: $highlight-addition

  pre .meta
    color: $highlight-purple

  pre
    .comment
      color: $highlight-comment

    .variable,
    .attribute,
    .regexp,
    .ruby .constant,
    .xml .tag .title,
    .xml .pi,
    .xml .doctype,
    .html .doctype,
    .css .id,
    .tag .name,
    .css .class,
    .css .pseudo
      color: $highlight-red

    .tag
      color: $highlight-aqua

    .number,
    .preprocessor,
    .literal,
    .params,
    .constant,
    .command
      color: $highlight-orange

    .built_in
      color: $highlight-yellow

    .ruby .class .title,
    .css .rules .attribute,
    .string,
    .value,
    .inheritance,
    .header,
    .ruby .symbol,
    .xml .cdata,
    .special,
    .number,
    .formula
      color: $highlight-green

    .keyword,
    .title,
    .css .hexcolor
      color: $highlight-aqua

    .function,
    .python .decorator,
    .python .title,
    .ruby .function .title,
    .ruby .title .keyword,
    .perl .sub,
    .javascript .title,
    .coffeescript .title
      color: $highlight-blue

    .tag .attr,
    .javascript .function
      color: $highlight-purple

```

### 文件路径: `themes\butterfly\source\css\_highlight\highlight\index.styl`
```styl
if $highlight_theme != false
  @require 'diff'

.container
  figure.highlight
    .line
      if wordWrap
        &:before
          display: inline-block
          padding: 0 6px 0 0
          min-width: 30px
          color: var(--hlnumber-color)
          content: counter(line)
          counter-increment: line
          text-align: left

      &.marked
        background-color: $highlight-selection

    table
      display: block
      overflow: auto
      border: none

      td
        padding: 0
        border: none

    .gutter pre
      padding-right: 10px
      padding-left: 10px
      background-color: var(--hlnumber-bg)
      color: var(--hlnumber-color)
      text-align: right

    .code pre
      padding-right: 10px
      padding-left: 10px
      width: 100%

```

### 文件路径: `themes\butterfly\source\css\_highlight\prismjs\diff.styl`
```styl
if $highlight_theme == 'light'
  // prism-base16-ateliersulphurpool.light
  pre[class*='language-']
    .token.function
      color: #ffb62c

    .token.comment,
    .token.prolog,
    .token.doctype,
    .token.cdata
      color: rgba(149, 165, 166, .8)

    .token.punctuation
      color: #5e6687

    .token.namespace
      opacity: .7

    .token.operator,
    .token.boolean,
    .token.number
      color: #c76b29

    .token.property
      color: #c08b30

    .token.tag
      color: #3d8fd1

    .token.string
      color: #22a2c9

    .token.selector
      color: #6679cc

    .token.attr-name
      color: #c76b29

    .token.entity,
    .token.url,
    .language-css .token.string,
    .style .token.string
      color: #22a2c9

    .token.attr-value,
    .token.keyword,
    .token.control,
    .token.directive,
    .token.unit
      color: #ac9739

    .token.statement,
    .token.regex,
    .token.atrule
      color: #22a2c9

    .token.placeholder,
    .token.variable
      color: #3d8fd1

    .token.deleted
      text-decoration: line-through

    .token.inserted
      border-bottom: 1px dotted #202746
      text-decoration: none

    .token.italic
      font-style: italic

    .token.important,
    .token.bold
      font-weight: bold

    .token.important
      color: #c94922

    .token.entity
      cursor: help

    pre > code.highlight
      outline: .4em solid #c94922
      outline-offset: .4em

if $highlight_theme == 'darker'
  // prism-atom-dark
  pre[class*='language-']
    .token.comment,
    .token.prolog,
    .token.doctype,
    .token.cdata
      color: #7C7C7C

    .token.punctuation
      color: #c5c8c6

    .namespace
      opacity: .7

    .token.property,
    .token.keyword,
    .token.tag
      color: #96CBFE

    .token.class-name
      color: #FFFFB6

    .token.boolean,
    .token.constant
      color: #99CC99

    .token.symbol,
    .token.deleted
      color: #f92672

    .token.number
      color: #FF73FD

    .token.selector,
    .token.attr-name,
    .token.string,
    .token.char,
    .token.builtin,
    .token.inserted
      color: #A8FF60

    .token.variable
      color: #C6C5FE

    .token.operator
      color: #EDEDED

    .token.entity
      color: #FFFFB6
      cursor: help

    .token.url
      color: #96CBFE

    .language-css .token.string,
    .style .token.string
      color: #87C38A

    .token.atrule,
    .token.attr-value
      color: #F9EE98

    .token.function
      color: #DAD085

    .token.regex
      color: #E9C062

    .token.important
      color: #fd971f

    .token.important,
    .token.bold
      font-weight: bold

    .token.italic
      font-style: italic

if $highlight_theme == 'pale night'
  // prism-dracula
  pre[class*='language-']
    .token.comment,
    .token.prolog,
    .token.doctype,
    .token.cdata
      color: #6272a4

    .token.punctuation
      color: #f8f8f2

    .namespace
      opacity: .7

    .token.property,
    .token.tag,
    .token.constant,
    .token.symbol,
    .token.deleted
      color: #ff79c6

    .token.boolean,
    .token.number
      color: #bd93f9

    .token.selector,
    .token.attr-name,
    .token.string,
    .token.char,
    .token.builtin,
    .token.inserted
      color: #50fa7b

    .token.operator,
    .token.entity,
    .token.url,
    .language-css .token.string,
    .style .token.string,
    .token.variable
      color: #f8f8f2

    .token.atrule,
    .token.attr-value,
    .token.function,
    .token.class-name
      color: #f1fa8c

    .token.keyword
      color: #8be9fd

    .token.regex,
    .token.important
      color: #ffb86c

    .token.important,
    .token.bold
      font-weight: bold

    .token.italic
      font-style: italic

    .token.entity
      cursor: help

if $highlight_theme == 'ocean'
  // prism-material-oceanic
  pre[class*='language-']
    &.language-css > code,
    &.language-sass > code,
    &.language-scss > code
      color: #fd9170 !important

    .namespace
      opacity: .7

    .token.atrule,
    .token.symbol,
    .token.constant,
    .token.boolean,
    .token.function
      color: #c792ea

    .token.attr-name,
    .token.builtin,
    .token.class
      color: #ffcb6b

    .token.attr-value,
    .token.attribute,
    .token.pseudo-class,
    .token.pseudo-element,
    .token.string
      color: #c3e88d

    .token.cdata,
    .token.property,
    .token.char,
    .token.inserted
      color: #80cbc4

    .token.class-name,
    .token.color,
    .token.hexcode,
    .token.regex
      color: #f2ff00

    .token.comment,
    .token.prolog,
    .token.doctype
      color: #546e7a

    .token.deleted,
    .token.variable,
    .token.entity,
    .token.selector,
    .token.tag,
    .token.unit
      color: #f07178

    .token.id
      color: #c792ea
      font-weight: bold

    .token.important
      color: #c792ea
      font-weight: bold

    .token.keyword
      color: #c792ea
      font-style: italic

    .token.number,
    .token.url
      color: #fd9170

    .token.operator,
    .token.punctuation
      color: #89ddff
```

### 文件路径: `themes\butterfly\source\css\_highlight\prismjs\index.styl`
```styl
if $prismjs_line_number
  @require 'line-number'

if $highlight_theme != false
  @require 'diff'

.container
  pre[class*='language-']
    // scrollbar - firefox
    @-moz-document url-prefix()
      scrollbar-color: var(--hlscrollbar-bg) transparent

    &::-webkit-scrollbar-thumb
      background: var(--hlscrollbar-bg)

    &:not(.line-numbers)
      padding: 10px 20px

    .caption
      margin-left: -3.8em
      padding: 4px 16px !important

      a
        padding: 0 !important

```

### 文件路径: `themes\butterfly\source\css\_highlight\prismjs\line-number.styl`
```styl
.container
  pre[class*='language-']
    &.line-numbers
      position: relative
      padding-left: 3.8em
      counter-reset: linenumber
      line-height: $line-height-code-block

      > code
        position: relative
        line-height: $line-height-code-block

        if hexo-config('code_blocks.word_wrap')
          white-space: pre-wrap
        else
          white-space: inherit
          word-wrap: normal
          word-break: normal
          overflow-wrap: normal

      .line-numbers-rows
        position: absolute
        top: 0
        left: -3.8em
        width: 3em
        letter-spacing: -1px
        font-size: 100%
        pointer-events: none
        user-select: none
        -webkit-user-select: none

        & > span
          display: block
          counter-increment: linenumber
          pointer-events: none

          &:before
            display: block
            padding-right: .8em
            color: var(--hlnumber-color)
            content: counter(linenumber)
            text-align: right

```

### 文件路径: `themes\butterfly\source\css\_layout\aside.styl`
```styl
#aside-content
  width: 26%

  +minWidth900()
    if hexo-config('aside.position') == 'right'
      padding-left: 15px
    else
      padding-right: 15px

  +maxWidth900()
    margin-top: 20px
    width: 100%

  .card-widget
    @extend .cardHover
    position: relative
    overflow: hidden
    margin-bottom: 20px
    padding: 20px 24px

    if hexo-config('aside.mobile') == false
      +maxWidth768()
        &:not(#card-toc)
          display: none

    &:last-child
      margin-bottom: 0

  .card-info
    .author-info
      &-name
        font-weight: 500
        font-size: 1.57em

      &-description
        margin-top: -.42em

    .site-data
      margin: 14px 0 4px

    .card-info-social-icons
      margin: 6px 0 -6px

      .social-icon
        margin: 0 10px
        color: var(--font-color)
        font-size: 1.4em

      i
        transition: all .3s

        &:hover
          transform: rotate(360deg)

    #card-info-btn
      display: block
      margin-top: 14px
      background-color: var(--btn-bg)
      color: var(--btn-color)
      text-align: center
      line-height: 2.4
      addBorderRadius(7)

      &:hover
        background-color: var(--btn-hover-color)

      span
        padding-left: 10px

  .item-headline
    padding-bottom: 6px
    font-size: 1.2em

    span
      margin-left: 6px

  .sticky_layout
    +minWidth900()
      position: sticky
      position: -webkit-sticky
      top: 20px
      transition: top .3s

  .card-tag-cloud
    a
      display: inline-block
      padding: 0 4px
      line-height: 1.8

      &:hover
        color: $text-hover !important

  .aside-list
    & > span
      display: block
      margin-bottom: 10px
      text-align: center

    & > .aside-list-item
      display: flex
      align-items: center
      padding: 6px 0

      &:first-child
        padding-top: 0

      &:not(:last-child)
        border-bottom: 1px dashed #f5f5f5

      &:last-child
        padding-bottom: 0

      .thumbnail
        overflow: hidden
        width: w = 4em
        height: w
        addBorderRadius()

        :first-child
          @extend .imgHover

      .content
        flex: 1
        padding-left: 10px
        word-break: break-all

        & > .name
          @extend .limit-more-line
          -webkit-line-clamp: 1

        & > time,
        & > .name
          display: block
          color: var(--card-meta)
          font-size: .85em

        & > .title,
        & > .comment
          @extend .limit-more-line
          color: var(--font-color)
          // font-size: 95%
          line-height: 1.5
          -webkit-line-clamp: 2

          &:hover
            color: $text-hover

      &.no-cover
        min-height: 4.4em

  .card-archives ul.card-archive-list,
  .card-categories ul.card-category-list
    margin: 0
    padding: 0
    list-style: none

  .card-archives ul.card-archive-list > .card-archive-list-item,
  .card-categories ul.card-category-list > .card-category-list-item
    a
      display: flex
      flex-direction: row
      margin: 2px 0
      padding: 2px 8px
      color: var(--font-color)
      transition: all .3s
      addBorderRadius()

      &:hover
        padding: 2px 12px
        background-color: var(--text-bg-hover)
        color: var(--white)

      span
        @extend .limit-one-line

        &:first-child
          flex: 1

  .card-categories
    .card-category-list
      &.child
        padding: 0 0 0 16px

      > .parent
        > a
          &.expand
            i
              transform: rotate(-90deg)

            & + .child
              display: block

          .card-category-list
            &-name
              width: 70% !important

            &-count
              width: calc(100% - 70% - 20px)
              text-align: right

          i
            float: right
            margin-right: -.5em
            padding: .5em
            transition: transform .3s
            transform: rotate(0)

        if hexo-config('aside.card_categories.expand') == false
          > .child
            display: none

  .card-webinfo
    .webinfo
      .webinfo-item
        display: flex
        align-items: center
        padding: 2px 10px 0

        div
          &:first-child
            flex: 1
            padding-right: 20px

  // toc
  #card-toc
    +minWidth901()
      right: 0 !important

    +maxWidth900()
      position: fixed
      right: 55px
      bottom: 30px
      z-index: 100
      max-width: $toc-mobile-maxWidth
      max-height: calc(100% - 60px)
      width: $toc-mobile-width
      transition: none
      transform: scale(0)
      transform-origin: right bottom

      &.open
        transform: scale(1)

    .toc-percentage
      float: right
      margin-top: -9px
      color: #a9a9a9
      font-style: italic
      font-size: 140%

    .toc-content
      overflow-y: scroll
      overflow-y: overlay
      margin: 0 -24px
      max-height: calc(100vh - 120px)
      width: calc(100% + 48px)

      +maxWidth900()
        max-height: calc(100vh - 140px)

      & > *
        margin: 0 20px !important

        & > .toc-item > .toc-child
          margin-left: 10px
          padding-left: 10px
          border-left: 1px solid var(--dark-grey)

      &:not(.is-expand)
        .toc-child
          display: none

          +maxWidth900()
            display: block !important

        .toc-item
          &.active
            .toc-child
              display: block

      ol,
      li
        list-style: none

      > ol
        padding: 0 !important

      ol
        margin: 0
        padding-left: 18px

      .toc-link
        display: block
        margin: 4px 0
        padding: 1px 8px
        color: var(--toc-link-color)
        transition: all .2s ease-in-out
        addBorderRadius()

        &:hover
          color: $theme-color

        &.active
          background: $theme-toc-color
          color: $toc-active-color

  .sticky_layout:only-child
    > :first-child
      margin-top: 0

  .card-more-btn
    float: right
    color: inherit

    &:hover
      animation: more-btn-move 1s infinite

  .card-announcement
    .item-headline
      i
        color: #FF0000

.avatar-img
  overflow: hidden
  margin: 0 auto
  width: 110px
  height: 110px
  border-radius: 70px

  img
    width: 100%
    height: 100%
    transition: filter 375ms ease-in .2s, transform .3s
    object-fit: cover

    &:hover
      transform: rotate(360deg)

.site-data
  display: table
  width: 100%
  table-layout: fixed

  & > a
    display: table-cell

    div
      transition: all .3s

    &:hover
      div
        color: $theme-color !important

    .headline
      @extend .limit-one-line
      color: var(--font-color)
      font-size: .95em

    .length-num
      margin-top: -.45em
      color: var(--text-highlight-color)
      font-size: 1.2em

@keyframes more-btn-move
  0%,
  100%
    transform: translateX(0)

  50%
    transform: translateX(3px)

@keyframes toc-open
  0%
    transform: scale(.7)

  100%
    transform: scale(1)

@keyframes toc-close
  0%
    transform: scale(1)

  100%
    transform: scale(.7)

+minWidth900()
  html.hide-aside
    .layout
      justify-content: center

      > .aside-content
        display: none

      > div:first-child
        width: 80%

.page
  .sticky_layout
    display: flex
    flex-direction: column

  if hexo-config('aside.card_recent_post.sort_order')
    .card-recent-post
      order: hexo-config('aside.card_recent_post.sort_order')

  if hexo-config('aside.card_newest_comments.sort_order')
    #card-newest-comments
      order: hexo-config('aside.card_newest_comments.sort_order')

  if hexo-config('aside.card_categories.sort_order')
    .card-categories
      order: hexo-config('aside.card_categories.sort_order')

  if hexo-config('aside.card_tags.sort_order')
    .card-tags
      order: hexo-config('aside.card_tags.sort_order')

  if hexo-config('aside.card_archives.sort_order')
    .card-archives
      order: hexo-config('aside.card_archives.sort_order')

  if hexo-config('aside.card_webinfo.sort_order')
    .card-webinfo
      order: hexo-config('aside.card_webinfo.sort_order')

```

### 文件路径: `themes\butterfly\source\css\_layout\chat.styl`
```styl
// chat
if hexo-config('chat.rightside_button') == true
  if hexo-config('chat.use') == 'chatra'
    #chatra:not(.chatra--expanded)
      visibility: hidden !important
      width: 1px !important
      height: 1px !important
      opacity: 0 !important
      pointer-events: none
```

### 文件路径: `themes\butterfly\source\css\_layout\comments.styl`
```styl
#post-comment
  .comment-head
    margin-bottom: 20px

    &:after
      display: block
      clear: both
      content: ''

    .comment-headline
      display: inline-block
      vertical-align: middle
      font-weight: 700
      font-size: 1.43em

    .comment-switch
      display: inline-block

      if hexo-config('comments.text')
        float: right
        margin: 2px auto 0
        padding: 4px 16px
        width: max-content
        border-radius: 8px
        background: $comments-switch-bg
      else
        vertical-align: middle

        > span
          display: none

      .first-comment
        color: $comments-switch-first-text

      .second-comment
        color: $comments-switch-second-text

      #switch-btn
        position: relative
        display: inline-block
        margin: -4px 8px 0
        width: 42px
        height: 22px
        border-radius: 34px
        background-color: $comments-switch-first-text
        vertical-align: middle
        cursor: pointer
        transition: .4s

        &:before
          position: absolute
          bottom: 4px
          left: 4px
          width: 14px
          height: 14px
          border-radius: 50%
          background-color: $comments-switch-round
          content: ''
          transition: .4s

  .comment-wrap
    > div
      animation: tabshow .5s

      &:nth-child(2)
        display: none

  &.move
    #switch-btn
      background-color: $comments-switch-second-text

      &:before
        transform: translateX(20px)

    .comment-wrap
      > div
        &:first-child
          display: none

        &:last-child
          display: block
```

### 文件路径: `themes\butterfly\source\css\_layout\footer.styl`
```styl
#footer
  position: relative
  background-color: $light-blue
  background-attachment: scroll
  background-position: bottom
  background-size: cover

  if hexo-config('footer_img') != false && hexo-config('mask.footer')
    &:before
      position: absolute
      width: 100%
      height: 100%
      background-color: var(--mark-bg)
      content: ''

#footer-wrap
  position: relative
  padding: 40px 20px
  color: var(--light-grey)
  text-align: center

  a
    color: var(--light-grey)

    &:hover
      text-decoration: underline

  .footer-separator
    margin: 0 4px

  .icp-icon
    padding: 0 4px
    max-height: 1.4em
    width: auto
    vertical-align: text-bottom

```

### 文件路径: `themes\butterfly\source\css\_layout\head.styl`
```styl
#page-header
  position: relative
  width: 100%
  background-color: $light-blue
  background-position: center center
  background-size: cover
  background-repeat: no-repeat
  transition: all .5s

  if hexo-config('mask.header')
    &:not(.not-top-img):before
      position: absolute
      width: 100%
      height: 100%
      background-color: var(--mark-bg)
      content: ''

  // index
  &.full_page
    height: $index_top_img_height
    background-attachment: fixed

    #site-info
      position: absolute
      top: $index_site_info_top
      padding: 0 10px
      width: 100%

  #site-title,
  #site-subtitle,
  #scroll-down .scroll-down-effects
    text-align: center
    text-shadow: 2px 2px 4px rgba(0, 0, 0, .15)
    line-height: 1.5

  #site-title
    margin: 0
    color: var(--white)
    font-size: 1.85em

    +minWidth768()
      font-size: 2.85em

  #site-subtitle
    color: var(--light-grey)
    font-size: 1.15em

    +minWidth768()
      font-size: 1.72em

  #site_social_icons
    display: none
    margin: 0 auto
    text-align: center

    +maxWidth768()
      display: block

    .social-icon
      margin: 0 10px
      color: var(--light-grey)
      text-shadow: 2px 2px 4px rgba(0, 0, 0, .15)
      font-size: 1.43em

  #scroll-down
    position: absolute
    bottom: 10px
    width: 100%
    cursor: pointer

    .scroll-down-effects
      position: relative
      width: 100%
      color: var(--light-grey)
      font-size: 20px

  // page
  &.not-home-page
    height: 400px

    +maxWidth768()
      height: 280px

  #page-site-info
    position: absolute
    top: 200px
    padding: 0 10px
    width: 100%

    +maxWidth768()
      top: 140px

  // post
  &.post-bg
    height: 400px

    +maxWidth768()
      height: 360px

  #post-info
    position: absolute
    width: 100%

    if hexo-config('post_meta.post.position') == 'center'
      top: calc(50% + 30px)
      padding: 0 8%
      text-align: center
      transform: translateY(-50%)

      +maxWidth768()
        padding: 0 15px
    else
      bottom: 30px

      & > *
        margin: 0 auto
        padding: 0 15px
        max-width: 1200px

        @media screen and (min-width: 768px) and (max-width: 1300px)
          padding: 0 30px

        +minWidth2000()
          max-width: 70%

  &.not-top-img
    margin-bottom: 10px
    height: 60px
    background: 0

    .title-seo
      display: none

    #nav
      background: rgba(255, 255, 255, .8)
      box-shadow: 0 5px 6px -5px rgba(133, 133, 133, .6)

      a,
      span.site-page,
      .site-name
        color: var(--font-color)
        text-shadow: none

  &.nav-fixed
    #nav
      position: fixed
      top: -60px
      z-index: 91
      background: rgba(255, 255, 255, .7)
      box-shadow: 0 5px 6px -5px alpha($grey, .6)
      transition: transform .2s ease-in-out, opacity .2s ease-in-out
      will-change: transform
      backdrop-filter: blur(7px)

      #blog-info
        color: var(--font-color)

        &:hover
          color: $light-blue

        .site-name
          text-shadow: none

        & > a:first-child
          display: none

        & > a:last-child
          display: inline

      a,
      span.site-page,
      #toggle-menu
        color: var(--font-color)
        text-shadow: none

        &:hover
          color: $light-blue

    &.fixed
      #nav
        top: 0
        transition: all .5s

  &.nav-visible:not(.fixed)
    #nav
      transition: all .5s
      transform: translate3d(0, 100%, 0)

    & + .layout
      & > .aside-content > .sticky_layout
        top: 70px
        transition: top .5s

  &.fixed
    #nav
      position: fixed

    & + .layout
      & > .aside-content > .sticky_layout
        top: 70px
        transition: top .5s

      #card-toc
        .toc-content
          max-height: calc(100vh - 170px)

#page
  .page-title
    margin: 0 0 10px
    font-weight: bold
    font-size: 2em

// for not top_img
#post
  & > #post-info
    margin-bottom: 30px

    .post-title
      padding-bottom: 4px
      border-bottom: 1px solid var(--light-grey)
      color: var(--text-highlight-color)

      .post-edit-link
        float: right

    #post-meta,
    #post-meta a
      color: #78818a

#post-info
  .post-title
    @extend .limit-more-line
    margin-bottom: 8px
    color: var(--white)
    font-weight: normal
    font-size: 2.5em
    line-height: 1.5
    -webkit-line-clamp: 3

    +maxWidth768()
      font-size: 2.1em

    .post-edit-link
      padding-left: 10px

  #post-meta
    color: var(--light-grey)
    font-size: 95%

    +minWidth768()
      > .meta-secondline
        > span:first-child
          display: none

    +maxWidth768()
      font-size: 90%

      > .meta-firstline,
      > .meta-secondline
        display: inline

    .post-meta
      &-separator
        margin: 0 5px

      &-icon
        margin-right: 4px

      &-label
        if hexo-config('post_meta.post.label')
          margin-right: 4px
        else
          display: none

    a
      color: var(--light-grey)
      transition: all .3s ease-out

      &:hover
        color: $text-hover
        text-decoration: underline

    if hexo-config('post_meta.post.date_format') == 'relative'
      time
        display: none

#nav
  position: absolute
  top: 0
  z-index: 90
  display: flex
  align-items: center
  padding: 0 36px
  width: 100%
  height: 60px
  font-size: 1.3em
  opacity: 0
  transition: all .5s

  +maxWidth768()
    padding: 0 16px

  &.show
    opacity: 1

  #blog-info
    flex: 1
    color: var(--light-grey)
    @extend .limit-one-line

    .site-icon
      margin-right: 6px
      height: 36px
      vertical-align: middle

    .nav-page-title
      display: none

  #toggle-menu
    display: none
    padding: 2px 0 0 6px
    vertical-align: top

    &:hover
      color: var(--white)

  a,
  span.site-page
    color: var(--light-grey)

    &:hover
      color: var(--white)

  .site-name
    text-shadow: 2px 2px 4px rgba($dark-black, .15)
    font-weight: bold

  .menus_items
    display: inline

    .menus_item
      position: relative
      display: inline-block
      padding: 0 0 0 14px

      &:hover
        .menus_item_child
          display: block

        & > span > i:last-child
          transform: rotate(180deg)

      & > span > i:last-child
        padding: 4px
        transition: transform .3s

      .menus_item_child
        position: absolute
        right: 0
        display: none
        margin-top: 8px
        padding: 0
        width: max-content
        background-color: var(--sidebar-bg)
        box-shadow: 0 5px 20px -4px rgba($dark-black, .5)
        animation: sub_menus .3s .1s ease both
        addBorderRadius(5)

        &:before
          position: absolute
          top: -8px
          left: 0
          width: 100%
          height: 20px
          content: ''

        li
          list-style: none

          &:hover
            background: var(--text-bg-hover)

          if hexo-config('rounded_corners_ui')
            &:first-child
              border-top-left-radius: 5px
              border-top-right-radius: 5px

            &:last-child
              border-bottom-right-radius: 5px
              border-bottom-left-radius: 5px

          a
            display: inline-block
            padding: 8px 16px
            width: 100%
            color: var(--font-color) !important
            text-shadow: none !important

  &.hide-menu
    #toggle-menu
      display: inline-block !important

      .site-page
        font-size: inherit

    .menus_items
      display: none

    #search-button span:not(.site-page)
      display: none

  #search-button
    display: inline
    padding: 0 0 0 14px

  .site-page
    position: relative
    padding-bottom: 6px
    text-shadow: 1px 1px 2px rgba($dark-black, .3)
    font-size: .78em
    cursor: pointer

    &:not(.child)
      &:after
        position: absolute
        bottom: 0
        left: 0
        z-index: -1
        width: 0
        height: 3px
        background-color: lighten($theme-color, 30%)
        content: ''
        transition: all .3s ease-in-out
        addBorderRadius()

      &:hover
        &:after
          width: 100%
```

### 文件路径: `themes\butterfly\source\css\_layout\loading.styl`
```styl
if hexo-config('preloader.enable') && hexo-config('preloader.source') == 1
  .loading-bg
    position: fixed
    z-index: 1000
    width: 50%
    height: 100%
    background-color: var(--preloader-bg)

  #loading-box
    .loading-left-bg
      @extend .loading-bg

    .loading-right-bg
      @extend .loading-bg
      right: 0

    .spinner-box
      position: fixed
      z-index: 1001
      display: flex
      justify-content: center
      align-items: center
      width: 100%
      height: 100vh

      .configure-border-1
        position: absolute
        padding: 3px
        width: 115px
        height: 115px
        background: #ffab91
        animation: configure-clockwise 3s ease-in-out 0s infinite alternate

      .configure-border-2
        left: -115px
        padding: 3px
        width: 115px
        height: 115px
        background: rgb(63, 249, 220)
        transform: rotate(45deg)
        animation: configure-xclockwise 3s ease-in-out 0s infinite alternate

      .loading-word
        position: absolute
        color: var(--preloader-color)
        font-size: 16px

      .configure-core
        width: 100%
        height: 100%
        background-color: var(--preloader-bg)

    &.loaded
      .loading-left-bg
        transition: all .5s
        transform: translate(-100%, 0)

      .loading-right-bg
        transition: all .5s
        transform: translate(100%, 0)

      .spinner-box
        display: none

  @keyframes configure-clockwise
    0%
      transform: rotate(0)

    25%
      transform: rotate(90deg)

    50%
      transform: rotate(180deg)

    75%
      transform: rotate(270deg)

    100%
      transform: rotate(360deg)

  @keyframes configure-xclockwise
    0%
      transform: rotate(45deg)

    25%
      transform: rotate(-45deg)

    50%
      transform: rotate(-135deg)

    75%
      transform: rotate(-225deg)

    100%
      transform: rotate(-315deg)

```

### 文件路径: `themes\butterfly\source\css\_layout\pagination.styl`
```styl
#pagination
  .pagination
    margin-top: 20px
    text-align: center

  .page-number
    &.current
      background: $theme-paginator-color
      color: var(--white)

  .full-width
    width: 100% !important

  .pagination-related
    height: 150px

    +minWidth768()
      flex: 1

    .info-1
      .info-item-2
        -webkit-line-clamp: 1

    .info-2
      .info-item-1
        -webkit-line-clamp: 2

  &.pagination-post
    overflow: hidden
    margin-top: 40px
    width: 100%
    addBorderRadius()
    display: flex

    +maxWidth768()
      flex-direction: column

.layout
  .pagination
    & > *
      display: inline-block
      margin: 0 6px
      width: w = 2.5em
      height: w
      line-height: w

    & > *:not(.space)
      @extend .cardHover

      &:hover
        background: var(--btn-hover-color)
        color: var(--btn-color)

#archive
  .pagination
    margin-top: 30px

    & > *:not(.space)
      box-shadow: none

.pagination-related
  position: relative
  display: inline-block
  overflow: hidden
  background: $dark-black
  vertical-align: bottom
  @extend .postImgHover

  &.next-post
    .info
      text-align: right

  .info
    .info-1,
    .info-2
      @extend .verticalCenter
      padding: 20px 40px
      color: var(--white)
      transition: transform .3s, opacity .3s

    .info-1
      .info-item-1
        color: var(--light-grey)
        text-transform: uppercase
        font-size: 90%

      .info-item-2
        @extend .limit-more-line
        color: var(--white)
        font-weight: 500

    .info-2
      opacity: 0
      transform: translate(0, 0)

      .info-item-1
        @extend .limit-more-line

  &:not(.no-desc):hover
    .info-1
      opacity: 0
      transform: translate(0, -100%)

    .info-2
      opacity: 1
      transform: translate(0, -50%)
```

### 文件路径: `themes\butterfly\source\css\_layout\post.styl`
```styl
beautify()
  headStyle(fontsize)
    padding-left: unit(fontsize + 8, 'px')

    &:before
      font-size: unit(fontsize - 2, 'px')

    &:hover
      padding-left: unit(fontsize + 12, 'px')

  h1,
  h2,
  h3,
  h4,
  h5,
  h6
    transition: all .2s ease-out

    &:before
      position: absolute
      top: calc(50% - 7px)
      left: 0
      color: $title-prefix-icon-color
      content: $title-prefix-icon
      line-height: 1
      transition: all .2s ease-out
      @extend .fontawesomeIcon

    &:hover
      &:before
        color: $light-blue

  h1
    headStyle(20)

  h2
    headStyle(18)

  h3
    headStyle(16)

  h4
    headStyle(14)

  h5
    headStyle(12)

  h6
    headStyle(12)

  ol,
  ul
    p
      margin: 0 0 8px

  li
    &::marker
      color: $light-blue
      font-weight: 600
      font-size: 1.05em

    &:hover
      &::marker
        color: var(--pseudo-hover)

  ul > li
    list-style-type: circle

  hr
    @extend .custom-hr

.container
  word-wrap: break-word
  overflow-wrap: break-word

  if hexo-config('text_align_justify')
    text-align: justify

  a
    color: $theme-link-color

    &:hover
      text-decoration: underline

  img
    display: block
    margin: 0 auto 20px
    max-width: 100%
    transition: filter 375ms ease-in .2s
    addBorderRadius()

  p
    margin: 0 0 16px

  iframe
    margin: 0 0 20px

  kbd
    margin: 0 3px
    padding: 3px 5px
    border: 1px solid #b4b4b4
    background-color: #f8f8f8
    box-shadow: 0 1px 3px rgba(0, 0, 0, .25), 0 2px 1px 0 rgba(255, 255, 255, .6) inset
    color: #34495e
    white-space: nowrap
    font-weight: 600
    font-size: .9em
    font-family: Monaco, 'Ubuntu Mono', monospace
    line-height: 1em
    addBorderRadius(3)

  if hexo-config('anchor.click_to_scroll')
    h1,
    h2,
    h3,
    h4,
    h5,
    h6
      width: fit-content

      a:not(.headerlink)
        position: relative
        z-index: 10

      a.headerlink
        position: absolute
        top: 0
        right: 0
        bottom: 0
        left: 0
        width: 100%
        height: 100%

  ol,
  ul
    ol,
    ul
      padding-left: 20px

    li
      margin: 4px 0

    p
      margin: 0 0 8px

  > :last-child
    margin-bottom: 0 !important

  hr
    margin: 20px 0

  if hexo-config('beautify.enable')
    if hexo-config('beautify.field') == 'site'
      beautify()
    else if hexo-config('beautify.field') == 'post'
      &.post-content
        beautify()

#post
  .tag_share
    &:after
      display: block
      clear: both
      content: ''

    .post-meta
      &__tag-list
        display: inline-block

      &__tags
        display: inline-block
        margin: 8px 8px 8px 0
        padding: 0 12px
        width: fit-content
        border: 1px solid $light-blue
        border-radius: 12px
        color: $light-blue
        font-size: .85em
        transition: all .2s ease-in-out

        &:hover
          background: $light-blue
          color: var(--white)

    .post-share
      display: inline-block
      float: right
      margin: 8px 0 0
      width: fit-content

      .social-share
        font-size: .85em

        .social-share-icon
          margin: 0 4px
          width: w = 1.85em
          height: w
          font-size: 1.2em
          line-height: w

  .post-copyright
    position: relative
    margin: 40px 0 10px
    padding: 10px 16px
    border: 1px solid var(--light-grey)
    transition: box-shadow .3s ease-in-out
    addBorderRadius()

    &:before
      @extend .fontawesomeIcon
      position: absolute
      top: 2px
      right: 12px
      color: $theme-color
      content: '\f1f9'
      font-size: 1.3em

    &:hover
      box-shadow: 0 0 8px 0 rgba(232, 237, 250, .6), 0 2px 4px 0 rgba(232, 237, 250, .5)

    .post-copyright
      &-meta
        color: $light-blue
        font-weight: bold

        i
          margin-right: 3px

      &-info
        padding-left: 6px

        a
          text-decoration: underline
          word-break: break-word

          &:hover
            text-decoration: none

  #post-outdate-notice
    position: relative
    margin: 0 0 20px
    padding: .5em 1.2em
    background-color: $noticeOutdate-bg
    color: $noticeOutdate-color
    addBorderRadius(3)

    .num
      padding: 0 4px

    if hexo-config('noticeOutdate.style') == 'flat'
      padding: .5em 1em .5em 2.6em
      border-left: 5px solid $noticeOutdate-border

      &:before
        @extend .fontawesomeIcon
        position: absolute
        top: 50%
        left: .9em
        color: $noticeOutdate-border
        content: '\f071'
        transform: translateY(-50%)

  .ads-wrap
    margin: 40px 0

```

### 文件路径: `themes\butterfly\source\css\_layout\relatedposts.styl`
```styl
.relatedPosts
  margin-top: 40px

  & > .headline
    margin-bottom: 5px
    font-weight: 700
    font-size: 1.43em

  & > .relatedPosts-list
    & > a
      margin: 3px
      width: calc(33.333% - 6px)
      height: 200px
      addBorderRadius()

      +maxWidth768()
        margin: 2px
        width: calc(50% - 4px)
        height: 150px

      +maxWidth600()
        width: calc(100% - 4px)

    .info
      .info-1
        .info-item-2
          -webkit-line-clamp: 2

      .info-2
        .info-item-1
          -webkit-line-clamp: 3
```

### 文件路径: `themes\butterfly\source\css\_layout\reward.styl`
```styl
.post-reward
  position: relative
  margin-top: 80px
  width: 100%
  text-align: center
  pointer-events: none

  & > *
    pointer-events: auto

  .reward-button
    display: inline-block
    padding: 4px 24px
    background: var(--btn-bg)
    color: var(--btn-color)
    cursor: pointer
    addBorderRadius()

    i
      margin-right: 5px

  &:hover
    .reward-button
      background: var(--btn-hover-color)

    & > .reward-main
      display: block

  .reward-main
    position: absolute
    bottom: 40px
    left: 0
    z-index: 100
    display: none
    padding: 0 0 15px
    width: 100%
    addBorderRadius()

    .reward-all
      display: inline-block
      margin: 0
      padding: 20px 10px
      background: var(--reward-pop)

      &:before
        position: absolute
        bottom: -10px
        left: 0
        width: 100%
        height: 20px
        content: ''

      &:after
        position: absolute
        right: 0
        bottom: 2px
        left: 0
        margin: 0 auto
        width: 0
        height: 0
        border-top: 13px solid var(--reward-pop)
        border-right: 13px solid transparent
        border-left: 13px solid transparent
        content: ''

      .reward-item
        display: inline-block
        padding: 0 8px
        list-style-type: none
        vertical-align: top

        img
          width: 130px
          height: 130px

        .post-qr-code-desc
          width: 130px
          color: $reward-pop-up-color

```

### 文件路径: `themes\butterfly\source\css\_layout\rightside.styl`
```styl
#rightside
  position: fixed
  right: -48px
  bottom: $rightside-bottom
  z-index: 100
  opacity: 0
  transition: all .5s

  &.rightside-show
    opacity: .8
    transform: translate(-58px, 0)

  #rightside-config-hide
    height: 0
    opacity: 0
    transition: transform .4s
    transform: translate(45px, 0)

    &.show
      height: auto
      opacity: 1
      transform: translate(0, 0)

    &.status
      height: auto
      opacity: 1

  & > div
    & > button,
    & > a
      display: block
      margin-bottom: 5px
      width: w = 35px
      height: w
      background-color: var(--btn-bg)
      color: var(--btn-color)
      text-align: center
      font-size: 16px
      line-height: w
      addBorderRadius(5)

      &:hover
        background-color: var(--btn-hover-color)

  #mobile-toc-button
    display: none

    +maxWidth900()
      display: block

  +maxWidth900()
    #hide-aside-btn
      display: none

  if hexo-config('rightside_scroll_percent')
    #go-up
      .scroll-percent
        display: none

      &.show-percent
        .scroll-percent
          display: block

          & + i
            display: none

      &:hover
        .scroll-percent
          display: none

          & + i
            display: block

```

### 文件路径: `themes\butterfly\source\css\_layout\sidebar.styl`
```styl
#sidebar
  #menu-mask
    position: fixed
    z-index: 102
    display: none
    width: 100%
    height: 100%
    background: alpha($dark-black, .8)

  #sidebar-menus
    position: fixed
    top: 0
    right: -($sidebar-width)
    z-index: 103
    overflow-x: hidden
    overflow-y: scroll
    padding-left: 5px
    width: $sidebar-width
    height: 100%
    background: var(--sidebar-bg)
    transition: all .5s

    &.open
      transform: translate3d(-100%, 0, 0)

    & > .avatar-img
      margin: 20px auto

    .site-data
      padding: 0 10px

    hr
      margin: 20px auto

    .menus_items
      margin: 20px
      padding: 15px
      background: var(--sidebar-menu-bg)
      box-shadow: 0 0 1px 1px rgba(7, 17, 27, .05)
      addBorderRadius(10)

      .site-page
        @extend .limit-one-line
        position: relative
        display: block
        margin: 4px 0
        padding: 2px 23px 2px 15px
        color: var(--font-color)
        font-size: 1.15em
        cursor: pointer
        addBorderRadius(6)

        &:hover
          background: var(--text-bg-hover)
          color: var(--white)

        i:first-child
          width: 15%
          text-align: left

        &.group
          & > i:last-child
            position: absolute
            top: .6em
            right: 10px
            transition: transform .3s

          &.hide
            & > i:last-child
              transform: rotate(90deg)

            & + .menus_item_child
              display: none

      .menus_item_child
        margin: 0
        padding-left: 25px
        list-style: none
```

### 文件路径: `themes\butterfly\source\css\_layout\third-party.styl`
```styl
#vcomment
  font-size: 1.1em

  .vbtn
    border: none
    background: var(--btn-bg)
    color: var(--btn-color)

    &:hover
      background: var(--btn-hover-color)

  .vimg
    transition: all .3s

    &:hover
      transform: rotate(360deg)

  .vcards .vcard .vcontent.expand
    &:before,
    &:after
      z-index: 22

#waline-wrap
  --waline-font-size: 1.1em
  --waline-theme-color: $button-bg
  --waline-active-color: $button-hover-color

  .wl-comment-actions > button:not(last-child)
    padding-right: 4px

if hexo-config('valine.bg')
  #vcomment
    textarea
      background: url(hexo-config('valine.bg')) 100% 100% no-repeat

      &:focus
        background-image: none

if hexo-config('waline.bg')
  #waline-wrap
    textarea
      background: url(hexo-config('waline.bg')) 100% 100% no-repeat

      &:focus
        background-image: none

.twikoo
  .tk-content
    p
      margin: 3px 0

.fireworks
  position: fixed
  top: 0
  left: 0
  z-index: $fireworks-zIndex
  pointer-events: none

.medium-zoom-image--opened
  z-index: 99999 !important
  margin: 0 !important

.medium-zoom-overlay
  z-index: 99999 !important

if hexo-config('mermaid.enable')
  .mermaid-wrap
    margin: 0 0 20px
    text-align: center

    & > svg
      height: 100%

  if hexo-config('mermaid.code_write')
    pre > code.mermaid
      display: none

if hexo-config('chartjs.enable')
  .chartjs-container
    display: flex
    flex-direction: column
    justify-content: center
    align-items: center
    margin: 0 0 20px
    text-align: center
    gap: 20px

    +maxWidth600()
      .chartjs-wrap
        width: 100% !important

    &.chartjs-abreast
      flex-direction: row

      +maxWidth600()
        flex-direction: column

    .chartjs-wrap
      width: -webkit-fill-available

    canvas
      display: inline-block !important

.utterances,
.fb-comments iframe
  width: 100% !important

#gitalk-container
  .gt-meta
    margin: 0 0 .8em
    padding: 6px 0 16px

if hexo-config('math.use')
  .katex-display
    overflow: auto hidden
    padding: 5px

    .katex-show
      display: block

  .katex
    display: none

    &.katex-show
      display: inline

  if hexo-config('math.hide_scrollbar')
    .katex-display,
    mjx-container
      scrollbar-width: none

      &::-webkit-scrollbar
        display: none

  // Mathjax
  mjx-container
    overflow-x: auto
    overflow-y: hidden
    padding-bottom: 4px
    max-width: 100%

    &[display]
      display: block !important
      min-width: auto !important

    &:not([display])
      display: inline-grid !important

  mjx-assistive-mml
    right: 0
    bottom: 0

.aplayer
  color: $font-black

.container
  .aplayer
    margin: 0 0 20px

    if hexo-config('beautify.enable')
      ol,
      ul
        margin: 0
        padding: 0

        li
          margin: 0
          padding: 0 15px

          &:before
            content: none

.snackbar-container.snackbar-css
  addBorderRadius(5)
  opacity: .85 !important

.abc-music-sheet
  margin: 0 0 20px
  opacity: 0
  transition: opacity .3s

  &.abcjs-container
    opacity: 1

+maxWidth768()
  .fancybox__toolbar__column.is-middle
    display: none
```

### 文件路径: `themes\butterfly\source\css\_mode\darkmode.styl`
```styl
if hexo-config('darkmode.enable') || hexo-config('display_mode') == 'dark'
  [data-theme='dark']
    --global-bg: darken(#121212, 2)
    --font-color: alpha(#FFFFFF, .7)
    --hr-border: alpha(#FFFFFF, .4)
    --hr-before-color: alpha(#FFFFFF, .7)
    --search-bg: #121212
    --search-input-color: alpha(#FFFFFF, .7)
    --search-a-color: alpha(#FFFFFF, .7)
    --preloader-bg: darken(#121212, 2)
    --preloader-color: alpha(#FFFFFF, .7)
    --tab-border-color: #2c2c2c
    --tab-botton-bg: #2c2c2c
    --tab-botton-color: alpha(#FFFFFF, .7)
    --tab-button-hover-bg: lighten(#121212, 15)
    --tab-button-active-bg: #121212
    --card-bg: #121212
    --sidebar-bg: #121212
    --sidebar-menu-bg: lighten(#121212, 5)
    --btn-hover-color: lighten(#121212, 40)
    --btn-color: alpha(#FFFFFF, .7)
    --btn-bg: lighten(#121212, 5)
    --text-bg-hover: lighten(#121212, 15)
    --light-grey: alpha(#FFFFFF, .7)
    --dark-grey: alpha(#FFFFFF, .2)
    --white: alpha(#FFFFFF, .9)
    --text-highlight-color: alpha(#FFFFFF, .9)
    --blockquote-color: alpha(#FFFFFF, .7)
    --blockquote-bg: lighten(#121212, 10)
    --reward-pop: lighten(#121212, 10)
    --toc-link-color: alpha(#FFFFFF, .6)
    --scrollbar-color: lighten(#121212, 25)
    --timeline-bg: lighten(#121212, 5)
    --zoom-bg: #121212
    --mark-bg: alpha($dark-black, .6)

    #web_bg:before
      position: absolute
      width: 100%
      height: 100%
      background-color: alpha($dark-black, .7)
      content: ''

    .container
      code
        background: #2c2c2c

      pre > code
        background: lighten(#121212, 2)

      figure.highlight
        box-shadow: none

      .note
        code
          background: $code-background

      .aplayer
        filter: brightness(.8)

      kbd
        border-color: #696969
        background-color: #525252
        color: #e2f1ff

    // 頭部
    #page-header
      &.nav-fixed > #nav,
      &.not-top-img > #nav
        background: alpha(#121212, .8)
        box-shadow: 0 5px 6px -5px rgba(133, 133, 133, 0)

    #post-comment
      .comment-switch
        if hexo-config('comments.text')
          background: #2c2c2c !important

        #switch-btn
          filter: brightness(.8)

    // note
    if hexo-config('note.style') == 'modern' || hexo-config('note.style') == 'flat'
      .note
        filter: brightness(.8)

    // hide-tags
    .hide-button,
    .btn-beautify,
    .hl-label,
    #post-outdate-notice,
    .error-img,
    .container iframe,
    .gist,
    .ads-wrap
      filter: brightness(.8)

    img
      if hexo-config('lazyload.enable') && hexo-config('lazyload.blur') && !hexo-config('lazyload.placeholder')
        filter: blur(0) brightness(.8)
      else
        filter: brightness(.8)

    #aside-content .aside-list > .aside-list-item:not(:last-child)
      border-bottom: 1px dashed alpha(#FFFFFF, .1)

    // Gitalk
    #gitalk-container
      filter: brightness(.8)

      svg
        fill: alpha(#FFFFFF, .9) !important

    // Disqusjs 反代模式下的適配
    #disqusjs
      #dsqjs
        &:hover,
        &:focus,
        .dsqjs-tab-active,
        .dsqjs-no-comment
          color: alpha(#FFFFFF, .7)

        .dsqjs-order-label
          background-color: lighten(#121212, 5)

        .dsqjs-post-body
          color: alpha(#FFFFFF, .7)

          code,
          pre
            background: #2c2c2c

          blockquote
            color: alpha(#FFFFFF, .7)

    #artitalk_main #lazy
      background: #121212

    #operare_artitalk .c2
      background: #121212

    #card-toc
      +maxWidth900()
        background: lighten(#121212, 5)

    // artalk
    .artalk.atk-dark-mode,
    .atk-layer-wrap.atk-dark-mode
      --at-color-font: alpha(#FFFFFF, .7)
      --at-color-meta: alpha(#FFFFFF, .7)
      --at-color-grey: alpha(#FFFFFF, .7)
    
    .atk-send-btn,
    .atk-badge
      color: alpha(#FFFFFF, .7) !important

    // waline
    #waline-wrap
      --waline-color: alpha(#FFFFFF, .7)
      --waline-dark-grey: alpha(#FFFFFF, .7)
      --waline-info-color: alpha(#FFFFFF, .5)
```

### 文件路径: `themes\butterfly\source\css\_mode\readmode.styl`
```styl
if hexo-config('readmode')
  .read-mode
    --font-color: #4c4948
    --readmode-light-color: #fff
    --white: #4c4948
    --light-grey: #4c4948
    --gray: #d6dbdf
    --hr-border: #d6dbdf
    --hr-before-color: darken(#d6dbdf, 10)
    --highlight-bg: #f7f7f7
    --exit-btn-bg: #C0C0C0
    --exit-btn-color: #fff
    --exit-btn-hover: darken(#C0C0C0, 20)
    --pseudo-hover: none

  [data-theme='dark']
    .read-mode
      --font-color: rgba(255, 255, 255, .7)
      --readmode-light-color: #0d0d0d
      --white: rgba(255, 255, 255, .9)
      --light-grey: rgba(255, 255, 255, .7)
      --gray: rgba(255, 255, 255, .7)
      --hr-border: rgba(255, 255, 255, .5)
      --hr-before-color: rgba(255, 255, 255, .7)
      --highlight-bg: #171717
      --exit-btn-bg: #1f1f1f
      --exit-btn-color: rgba(255, 255, 255, .9)
      --exit-btn-hover: lighten(#1f1f1f, 20)

  .read-mode
    background: var(--readmode-light-color)

    .exit-readmode
      position: fixed
      top: 30px
      right: 30px
      z-index: 100
      width: 40px
      height: 40px
      background: var(--exit-btn-bg)
      color: var(--exit-btn-color)
      font-size: 16px
      transition: background .3s
      addBorderRadius(8)

      +maxWidth768()
        top: initial
        bottom: 30px

      &:hover
        background: var(--exit-btn-hover)

    #aside-content
      display: none

    #page-header.post-bg
      background: none !important

      &:before
        opacity: 0

      & > #post-info
        text-align: center

    #post
      margin: 0 auto
      background: transparent
      box-shadow: none

      &:hover
        box-shadow: none

    & > canvas
      display: none !important

    .highlight-tools,
    #footer,
    #post > *:not(#post-info):not(.post-content),
    #nav,
    #post-outdate-notice,
    #web_bg,
    #rightside,
    .not-top-img
      display: none !important

    .container
      a
        color: #99a9bf

      pre,
      .highlight:not(.js-file-line-container)
        background: var(--highlight-bg) !important

        *
          color: var(--font-color) !important

      figure.highlight
        border-radius: 0 !important
        box-shadow: none !important

        & > :not(.highlight-tools)
          display: block !important

        .line:before
          color: var(--font-color) !important

        .hljs
          background: var(--highlight-bg) !important

      h1,
      h2,
      h3,
      h4,
      h5,
      h6
        padding: 0

        &:before
          content: ''

        &:hover
          padding: 0

      ul,
      li,
      ol
        &:hover:before
          transform: none !important

      ol,
      li
        &:before
          background: transparent !important
          color: var(--font-color) !important

      ul
        >li
          &:before
            border-color: var(--gray) !important

      .tabs
        border: 2px solid var(--tab-border-color)

        > .nav-tabs
          background: transparent

          > .tab
            border-top: none !important

        > .tab-contents .tab-item-content.active
          animation: none

      code
        color: var(--font-color)

      blockquote
        border-color: var(--gray)
        background-color: var(--readmode-light-color)

      kbd
        border: 1px solid var(--gray)
        background-color: transparent
        box-shadow: none
        color: var(--font-color)

      .hide-toggle
        border: 1px solid var(--gray) !important

      .hide-button,
      .btn-beautify,
      .hl-label
        border: 1px solid var(--gray) !important
        background: var(--readmode-light-color) !important
        color: var(--font-color) !important

      .note
        border: 2px solid var(--gray)
        border-left-color: var(--gray) !important
        filter: none
        background-color: var(--readmode-light-color) !important
        color: var(--font-color)

        &:before,
        .note-icon
          color: var(--font-color)

```

### 文件路径: `themes\butterfly\source\css\_page\404.styl`
```styl
if hexo-config('error_404.enable')
  .type-404
    .error-content
      @extend .cardHover
      overflow: hidden
      margin: 0 20px
      height: 360px

      +maxWidth768()
        margin: 0
        height: 500px

      .error-img
        display: inline-block
        overflow: hidden
        width: 50%
        height: 100%

        +maxWidth768()
          width: 100%
          height: 45%

        img
          @extend .imgHover
          background-color: $theme-color

      .error-info
        display: inline-flex
        flex-direction: column
        justify-content: center
        align-content: center
        width: 50%
        height: 100%
        vertical-align: top
        text-align: center

        if $site-name-font
          font-family: $site-name-font

        +maxWidth768()
          width: 100%
          height: 55%

        .error_title
          margin-top: -.6em
          font-size: 9em

          +maxWidth768()
            font-size: 8em

        .error_subtitle
          @extend .limit-more-line
          margin-top: -3em
          word-break: break-word
          font-size: 1.6em
          -webkit-line-clamp: 2

    .nc
      margin-top: 5%
      padding: 0 20px

    #footer
      display: none

    & + #rightside
      display: none
```

### 文件路径: `themes\butterfly\source\css\_page\archives.styl`
```styl
.article-sort
  margin-left: 10px
  padding-left: 20px
  border-left: 2px solid lighten($light-blue, 20)

  &-title
    position: relative
    margin-left: 10px
    padding-bottom: 20px
    padding-left: 20px
    font-size: 1.72em

    &:hover
      &:before
        border-color: var(--pseudo-hover)

    &:before
      position: absolute
      top: calc(((100% - 36px) / 2))
      left: -9px
      z-index: 1
      width: w = 10px
      height: h = w
      border: .5 * w solid $light-blue
      border-radius: w
      background: var(--card-bg)
      content: ''
      line-height: h
      transition: all .2s ease-in-out

    &:after
      position: absolute
      bottom: 0
      left: 0
      z-index: 0
      width: 2px
      height: 1.5em
      background: lighten($light-blue, 20)
      content: ''

  &-item
    position: relative
    display: flex
    align-items: center
    margin: 0 0 20px 10px
    transition: all .2s ease-in-out

    &:hover
      &:before
        border-color: var(--pseudo-hover)

    &:before
      $w = 6px
      position: absolute
      left: calc(-20px - 17px)
      width: w = $w
      height: h = w
      border: .5 * w solid $light-blue
      border-radius: w
      background: var(--card-bg)
      content: ''
      transition: all .2s ease-in-out

    &.no-article-cover
      height: 80px

      .article-sort-item-info
        padding: 0

    &.year
      font-size: 1.43em
      margin-bottom: 10px

      &:hover
        &:before
          border-color: $light-blue

      &:before
        border-color: var(--pseudo-hover)

    &-time
      color: var(--card-meta)
      font-size: .85em

      time
        padding-left: 6px
        cursor: default

    &-title
      @extend .limit-more-line
      color: var(--font-color)
      font-size: 1.05em
      transition: all .3s
      -webkit-line-clamp: 2

      &:hover
        color: $text-hover
        transform: translateX(10px)

    &-img
      overflow: hidden
      width: 100px
      height: 70px
      addBorderRadius()

      +maxWidth768()
        width: 70px
        height: 70px

      :first-child
        @extend .imgHover

    &-info
      flex: 1
      padding: 0 16px

```

### 文件路径: `themes\butterfly\source\css\_page\categories.styl`
```styl
.category-lists
  .category-title
    font-size: 2.57em

    +maxWidth768()
      font-size: 2em

  .category-list
    margin-bottom: 0

    a
      color: var(--font-color)

      &:hover
        color: $text-hover

    .category-list-count
      margin-left: 8px
      color: var(--card-meta)

      &:before
        content: '('

      &:after
        content: ')'

  ul
    padding: 0 0 0 20px
    @extend .list-beauty

    ul
      padding-left: 4px

    li
      position: relative
      margin: 6px 0
      padding: .12em .4em .12em 1.4em

```

### 文件路径: `themes\butterfly\source\css\_page\common.styl`
```styl
#body-wrap
  display: flex
  flex-direction: column
  min-height: 100vh

.layout
  display: flex
  flex: 1 auto
  margin: 0 auto
  padding: 40px 15px
  max-width: 1200px
  width: 100%

  +maxWidth900()
    flex-direction: column

  +maxWidth768()
    padding: 20px 5px

  +minWidth2000()
    max-width: 70%

  & > div:first-child:not(.nc)
    @extend .cardHover
    align-self: flex-start
    padding: 50px 40px

    +maxWidth768()
      padding: 36px 14px

  & > div:first-child
    width: 74%
    transition: all .3s

    +maxWidth900()
      width: 100% !important

    if hexo-config('aside.position') == 'left'
      +minWidth900()
        order: 2

  // 隱藏aside
  &.hide-aside
    max-width: 1000px

    +minWidth2000()
      max-width: 1300px

    & > div
      width: 100% !important

// for apple device
.apple
  #page-header.full_page
    background-attachment: scroll !important

  .recent-post-item,
  .avatar-img,
  .flink-item-icon
    transform: translateZ(0)

```

### 文件路径: `themes\butterfly\source\css\_page\flink.styl`
```styl
.container
  .flink
    margin-bottom: 20px

    .flink-list
      overflow: auto
      padding: 10px 10px 0
      text-align: center

      & > .flink-list-item
        position: relative
        float: left
        overflow: hidden
        margin: 15px 7px
        width: calc(100% / 3 - 15px)
        height: 90px
        line-height: 17px
        -webkit-transform: translateZ(0)
        addBorderRadius(8)

        +maxWidth1024()
          width: calc(50% - 15px) !important

        +maxWidth600()
          width: calc(100% - 15px) !important

        &:hover
          .flink-item-icon
            margin-left: -10px
            width: 0

        &:before
          position: absolute
          top: 0
          right: 0
          bottom: 0
          left: 0
          z-index: -1
          background: var(--text-bg-hover)
          content: ''
          transition: transform .3s ease-out
          transform: scale(0)

        &:hover:before,
        &:focus:before,
        &:active:before
          transform: scale(1)

        a
          color: var(--font-color)
          text-decoration: none

          .flink-item-icon
            float: left
            overflow: hidden
            margin: 15px 10px
            width: 60px
            height: 60px
            border-radius: 7px
            transition: width .3s ease-out

            img
              width: 100%
              height: 100%
              transition: filter 375ms ease-in .2s, transform .3s
              object-fit: cover

          .img-alt
            display: none

    .flink-item-name
      @extend .limit-one-line
      padding: 16px 10px 0 0
      height: 40px
      font-weight: bold
      font-size: 1.43em

    .flink-item-desc
      @extend .limit-one-line
      padding: 16px 10px 16px 0
      height: 50px
      font-size: .93em

    .flink-name
      margin-bottom: 5px
      font-weight: bold
      font-size: 1.5em
```

### 文件路径: `themes\butterfly\source\css\_page\homepage.styl`
```styl
$indexLayout = hexo-config('index_layout') || 1
$indexEnable = hexo-config('cover.index_enable')

#recent-posts
  .recent-post-item
    @extend .cardHover
    position: relative
    overflow: hidden
    margin-bottom: 20px

    if $indexLayout == 6 || ($indexLayout == 7)
      display: inline-block
      width: calc(100% / 2 - 8px)
      vertical-align: top

      +maxWidth768()
        width: 100%

      +minWidth2000()
        width: calc(100% / 3 - 8px)

    if $indexLayout == 1 || ($indexLayout == 2 || ($indexLayout == 3))
      display: flex
      flex-direction: row
      align-items: center
      height: 16.8em

      +maxWidth768()
        flex-direction: column
        height: auto

      +minWidth2000()
        height: 18.8em

    &:hover
      .post-bg
        transform: scale(1.1)

    &.ads-wrap
      display: block !important
      height: auto !important

    .post_cover
      overflow: hidden

      if ($indexLayout != 5 && ($indexLayout != 7))
        +maxWidth768()
          width: 100%
          height: 230px

      if $indexLayout == 1 || ($indexLayout == 2 || ($indexLayout == 3))
        width: 42%
        height: 100%

        &.right
          order: 1

          +maxWidth768()
            order: 0

      if $indexLayout == 4 || ($indexLayout == 5 || ($indexLayout == 6 || ($indexLayout == 7)))
        width: 100%

        if ($indexLayout == 5 || ($indexLayout == 7))
          height: 17em
        else
          height: 230px

      if ($indexLayout == 5 || ($indexLayout == 7)) && $indexEnable
        &:before
          position: absolute
          z-index: 1
          width: 100%
          height: 100%
          background-color: rgba(18, 18, 18, .4)
          content: ''
          backdrop-filter: blur(3px)

      .post-bg
        z-index: -4
        @extend .imgHover

    & >.recent-post-info
      +maxWidth768()
        padding: 20px 20px 30px
        width: 100%

      if $indexLayout == 1 || ($indexLayout == 2 || ($indexLayout == 3))
        padding: 0 40px
        width: 58%

      if $indexLayout == 4 || ($indexLayout == 5 || ($indexLayout == 6 || ($indexLayout == 7)))
        padding: 30px 30px 25px

      if ($indexLayout == 5 || ($indexLayout == 7)) && $indexEnable
        &:not(.no-cover)
          position: absolute
          top: 50%
          z-index: 2
          width: 100%
          color: var(--text-highlight-color)
          transform: translateY(-50%)
          --text-highlight-color: rgba(255, 255, 255, 1)
          --card-meta: rgba(255, 255, 255, .7)

      &.no-cover
        +maxWidth768()
          padding: 30px 20px

        if $indexLayout == 1 || ($indexLayout == 2 || ($indexLayout == 3))
          width: 100%

        if $indexLayout == 4 || ($indexLayout == 5 || ($indexLayout == 6 || ($indexLayout == 7)))
          padding: 35px 30px

      & > .article-title
        @extend .limit-more-line
        color: var(--text-highlight-color)
        font-size: 1.55em
        line-height: 1.4
        transition: all .2s ease-in-out
        -webkit-line-clamp: 2

        .sticky
          margin-right: 10px
          color: $sticky-color
          transform: rotate(45deg)

        +maxWidth768()
          font-size: 1.43em

        &:hover
          color: $text-hover

      & > .article-meta-wrap
        margin: 6px 0
        color: var(--card-meta)
        font-size: .9em

        & > .post-meta-date
          cursor: default

        i
          margin: 0 4px 0 0

        .fa-spinner
          margin: 0

        .article-meta-label
          if hexo-config('post_meta.page.label')
            padding-right: 4px
          else
            display: none

        .article-meta-separator
          margin: 0 6px

        .article-meta-link
          margin: 0 4px

        if hexo-config('post_meta.page.date_format') == 'relative'
          time
            display: none

        a
          color: var(--card-meta)

          &:hover
            color: $text-hover
            text-decoration: underline

      & > .content
        @extend .limit-more-line
        -webkit-line-clamp: 2
```

### 文件路径: `themes\butterfly\source\css\_page\shuoshuo.styl`
```styl
#article-container
  .shuoshuo-item
    @extend .cardHover
    margin-bottom: 20px
    padding: 35px 30px 30px

    +maxWidth768()
      padding: 25px 20px 20px

  .shuoshuo-item-header
    display: flex
    align-items: center
    cursor: default

  .shuoshuo-avatar
    overflow: hidden
    width: 40px
    height: 40px
    border-radius: 40px

    img
      margin: 0
      width: 100%
      height: 100%

  .shuoshuo-info
    margin-left: 10px
    line-height: 1.5

  .shuoshuo-date
    color: #858585
    font-size: .8em

  .shuoshuo-content
    padding: 15px 0 10px

    & > *:last-child
      margin-bottom: 0

  .shuoshuo-footer
    display: flex
    align-items: center

    &.flex-between
      justify-content: space-between

    &.flex-end
      justify-content: flex-end

    .shuoshuo-tag
      display: inline-block
      margin-right: 8px
      padding: 0 8px
      width: fit-content
      border: 1px solid $light-blue
      border-radius: 12px
      color: $light-blue
      font-size: .85em
      cursor: default
      transition: all .2s ease-in-out

      &:hover
        background: $light-blue
        color: var(--white)

    .shuoshuo-comment-btn
      padding: 2px
      color: #90a4ae
      cursor: pointer

      &:hover
        color: $light-blue

  .shuoshuo-comment
    padding-top: 10px

    &.no-comment
      display: none

```

### 文件路径: `themes\butterfly\source\css\_page\tags.styl`
```styl
.tag-cloud
  &-list
    a
      display: inline-block
      margin: 2px
      padding: 2px 7px
      line-height: 1.7
      transition: all .3s
      addBorderRadius(5)

      &:hover
        background: var(--btn-bg) !important
        box-shadow: 2px 2px 6px rgba(0, 0, 0, .2)
        color: var(--btn-color) !important

      +maxWidth768()
        zoom: .85

  &-title
    font-size: 2.57em

    +maxWidth768()
      font-size: 2em

.page-title
  & + .tag-cloud-list
    text-align: left

```

### 文件路径: `themes\butterfly\source\css\_search\algolia.styl`
```styl
#algolia-search
  .search-dialog
    .ais-SearchBox
      input
        padding: 5px 14px
        width: 100%
        outline: none
        border: 2px solid $search-color
        border-radius: 40px
        background: var(--search-bg)
        color: var(--search-input-color)

      .ais-SearchBox-loadingIndicator
        position: absolute
        top: 18px
        left: 67px

    .ais-Hits-list
      margin: 0
      padding: 0
      @extend .list-beauty

      a
        color: var(--search-a-color)

        &:hover
          color: $search-color

      mark
        background: transparent
        color: $search-keyword-highlight
        font-weight: bold

    .algolia-hits-item-title
      font-weight: 600

    .algolia-hit-item-content
      margin: 0 0 8px
      word-break: break-word

    .ais-Pagination
      margin: 15px 0 0
      padding: 0
      text-align: center

      .ais-Pagination-list
        margin: 0
        padding: 0
        list-style: none

      .ais-Pagination-item
        display: inline
        margin: 0 4px
        padding: 0

        .ais-Pagination-link
          display: inline-block
          min-width: 24px
          height: 24px
          text-align: center
          line-height: 24px
          addBorderRadius()

      .ais-Pagination-item--selected
        a
          background: $theme-paginator-color
          color: #eee
          cursor: default

      .ais-Pagination-item--disabled
        visibility: hidden

    #algolia-hits
      > div
        overflow-y: overlay
        margin: 0 -20px
        padding: 0 22px
        max-height: calc(80vh - 220px)

        +maxWidth768()
          max-height: none
          height: calc(var(--search-height) - 235px)

    #algolia-info
      div
        display: inline

      .algolia-poweredBy
        float: right
        vertical-align: text-top

        svg
          height: 1.1em
```

### 文件路径: `themes\butterfly\source\css\_search\index.styl`
```styl
.search-dialog
  position: fixed
  top: 10%
  left: 50%
  z-index: 1001
  display: none
  margin-left: -300px
  padding: 20px
  width: 600px
  background: var(--search-bg)
  --search-height: 100vh
  addBorderRadius(8)

  +maxWidth768()
    top: 0
    left: 0
    margin: 0
    width: 100%
    height: 100%
    border-radius: 0

  .search-nav
    margin: 0 0 14px
    color: $search-color
    font-size: 1.4em
    line-height: 1

    .search-dialog-title
      margin-right: 10px

    .search-close-button
      float: right
      color: $grey
      transition: color .2s ease-in-out

      &:hover
        color: $search-color
  
  hr
    margin: 15px auto
    @extend .custom-hr

#search-mask
  position: fixed
  top: 0
  right: 0
  bottom: 0
  left: 0
  z-index: 1000
  display: none
  background: rgba($dark-black, .6)

if hexo-config('search.use') == 'algolia_search'
  @require 'algolia'
else if hexo-config('search.use') == 'local_search'
  @require 'local-search'
```

### 文件路径: `themes\butterfly\source\css\_search\local-search.styl`
```styl
#local-search
  .search-dialog
    .local-search-box
      margin: 0 auto
      max-width: 100%
      width: 100%

      input
        padding: 5px 14px
        width: 100%
        outline: none
        border: 2px solid $search-color
        border-radius: 40px
        background: var(--search-bg)
        color: var(--search-input-color)
        -webkit-appearance: none

    .search-wrap
      display: none

    .local-search-hit-item
      margin-left: 24px
      padding-left: 3px
      line-height: 1.8

      &::marker
        color: $search-color
        font-weight: bold
        font-style: italic

      a
        color: var(--search-a-color)

        &:hover
          color: $search-color

      .search-result-title
        font-weight: 600

      .search-result
        margin: 0 0 8px
        word-break: break-all
        font-size: .9em

    .search-result-list
      overflow-y: overlay
      margin: 0 -20px
      padding: 0 22px
      max-height: calc(80vh - 180px)

      +maxWidth768()
        max-height: calc(var(--search-height) - 190px) !important

.search-keyword
  background: transparent
  color: $search-keyword-highlight
  font-weight: 600
```

### 文件路径: `themes\butterfly\source\css\_tags\button.styl`
```styl
.container
  .btn-center
    margin: 0 0 20px
    text-align: center

  .btn-beautify
    display: inline-block
    margin: 0 4px 6px
    padding: 0 15px
    background-color: var(--btn-beautify-color, $btn-default-color)
    color: $btn-color
    line-height: 2
    addBorderRadius()

    for $type in $color-types
      &.{$type}
        --btn-beautify-color: lookup('$tagsP-' + $type + '-color')

    &:hover
      background-color: var(--btn-hover-color)

    i + span
      margin-left: 6px

    &:not(.block) + .btn-beautify:not(.block)
      margin: 0 4px 20px

    &.block
      display: block
      margin: 0 0 20px
      width: fit-content
      width: -moz-fit-content

      &.center
        margin: 0 auto 20px

      &.right
        margin: 0 0 20px auto

    &.larger
      padding: 6px 15px

    &:hover
      text-decoration: none

    &.outline
      border: 1px solid transparent
      border-color: var(--btn-beautify-color, $btn-default-color)
      background-color: transparent
      color: var(--btn-beautify-color, $btn-default-color)

      &:hover
        background-color: var(--btn-beautify-color, $btn-default-color)

      &:hover
        color: white !important

```

### 文件路径: `themes\butterfly\source\css\_tags\gallery.styl`
```styl
.container
  figure.gallery-group
    position: relative
    float: left
    overflow: hidden
    margin: 6px 4px
    width: calc(50% - 8px)
    height: 250px
    border-radius: 10px
    background: $dark-black
    -webkit-transform: translate3d(0, 0, 0)

    +maxWidth600()
      width: calc(100% - 8px)

    +minWidth1024()
      width: calc(100% / 3 - 8px)

    &:hover
      img
        opacity: .4
        transform: translate3d(0, 0, 0)

      .gallery-group-name::after
        transform: translate3d(0, 0, 0)

      p
        opacity: 1
        transform: translate3d(0, 0, 0)

    img
      position: relative
      margin: 0
      max-width: none
      width: calc(100% + 20px)
      height: 250px
      backface-visibility: hidden
      opacity: .8
      transition: all .3s, filter 375ms ease-in .2s
      transform: translate3d(-10px, 0, 0)
      object-fit: cover

    figcaption
      position: absolute
      top: 0
      left: 0
      padding: 30px
      width: 100%
      height: 100%
      color: $gallery-color
      text-transform: uppercase
      backface-visibility: hidden

      & > a
        position: absolute
        top: 0
        right: 0
        bottom: 0
        left: 0
        z-index: 1000
        opacity: 0

    p
      @extend .limit-more-line
      margin: 0
      padding: 8px 0 0
      letter-spacing: 1px
      font-size: 1.1em
      line-height: 1.5
      opacity: 0
      transition: opacity .35s, transform .35s
      transform: translate3d(100%, 0, 0)
      -webkit-line-clamp: 4

    .gallery-group-name
      @extend .limit-more-line
      position: relative
      margin: 0
      padding: 8px 0
      font-weight: bold
      font-size: 1.65em
      line-height: 1.5
      -webkit-line-clamp: 2

      &:after
        position: absolute
        bottom: 0
        left: 0
        width: 100%
        height: 2px
        background: $gallery-color
        content: ''
        transition: transform .35s
        transform: translate3d(-100%, 0, 0)

  .gallery-group-main
    overflow: auto
    padding: 0 0 16px

  .gallery-container
    margin: 0 0 20px
    text-align: center
    opacity: 0

    &.loaded
      opacity: 1

    img
      display: initial
      margin: 0
      width: 100%
      height: 100%

    .gallery-data
      display: none

    button
      margin-top: 25px
      padding: 8px 14px
      background: var(--btn-bg)
      color: var(--btn-color)
      font-weight: bold
      font-size: 1.1em
      transition: all .3s
      addBorderRadius(5)

      &:hover
        background: var(--btn-hover-color)

        i
          margin-left: 8px

      i
        margin-left: 4px
        transition: all .3s

  .loading-container
    display: inline-block
    overflow: hidden
    width: 154px
    height: 154px

    .loading-item
      position: relative
      width: 100%
      height: 100%
      backface-visibility: hidden
      transform: translateZ(0) scale(1)
      transform-origin: 0 0

      div
        position: absolute
        width: 30.8px
        height: 30.8px
        border-radius: 50%
        background: #e15b64
        transform: translate(61.6px, 61.6px) scale(1)
        animation: loading-ball 1.92s infinite cubic-bezier(0, .5, .5, 1)

        &:nth-child(1)
          background: #f47e60
          transform: translate(113.96px, 61.6px) scale(1)
          animation: loading-ball-r .48s infinite cubic-bezier(0, .5, .5, 1), loading-ball-c 1.92s infinite step-start

        &:nth-child(2)
          background: #e15b64
          animation-delay: -.48s

        &:nth-child(3)
          background: #f47e60
          animation-delay: -.96s

        &:nth-child(4)
          background: #f8b26a
          animation-delay: -1.44s

        &:nth-child(5)
          background: #abbd81
          animation-delay: -1.92s

@keyframes loading-ball
  0%
    transform: translate(9.24px, 61.6px) scale(0)

  25%
    transform: translate(9.24px, 61.6px) scale(0)

  50%
    transform: translate(9.24px, 61.6px) scale(1)

  75%
    transform: translate(61.6px, 61.6px) scale(1)

  100%
    transform: translate(113.96px, 61.6px) scale(1)

@keyframes loading-ball-r
  0%
    transform: translate(113.96px, 61.6px) scale(1)

  100%
    transform: translate(113.96px, 61.6px) scale(0)

@keyframes loading-ball-c
  0%
    background: #e15b64

  25%
    background: #abbd81

  50%
    background: #f8b26a

  75%
    background: #f47e60

  100%
    background: #e15b64

```

### 文件路径: `themes\butterfly\source\css\_tags\hexo.styl`
```styl
// pullquote
blockquote
  &.pullquote
    position: relative
    max-width: 45%
    font-size: 110%

    &.left
      float: left
      margin: 1em .5em 0 0

    &.right
      float: right
      margin: 1em 0 0 .5em

// hexo tag video
.video-container
  position: relative
  overflow: hidden
  margin-bottom: 16px
  padding-top: 56.25%
  height: 0

  iframe
    position: absolute
    top: 0
    left: 0
    margin-top: 0
    width: 100%
    height: 100%

```

### 文件路径: `themes\butterfly\source\css\_tags\hide.styl`
```styl
// tag-hide
.hide-inline,
.hide-block
  & > .hide-button
    display: inline-block
    padding: 5px 18px
    background: $tag-hide-bg
    color: var(--white)
    addBorderRadius()

    &:hover
      background-color: var(--btn-hover-color)

    &.open
      display: none

      & + div
        display: block

      & + span
        display: inline

  & > .hide-content
    display: none

.hide-inline
  & > .hide-button
    margin: 0 6px

  & > .hide-content
    margin: 0 6px

.hide-block
  margin: 0 0 16px

.toggle
  margin-bottom: 20px
  border: 1px solid $tag-hide-toggle-bg
  addBorderRadius(5, true)

  & > .toggle-button
    padding: 6px 15px
    background: $tag-hide-toggle-bg
    color: #1F2D3D
    cursor: pointer

  & > .toggle-content
    margin: 30px 24px

```

### 文件路径: `themes\butterfly\source\css\_tags\inlineImg.styl`
```styl
.container
  .inline-img
    display: inline
    margin: 0 3px
    height: 1.1em
    vertical-align: text-bottom
```

### 文件路径: `themes\butterfly\source\css\_tags\label.styl`
```styl
.hl-label
  padding: 2px 4px
  color: $btn-color
  addBorderRadius(3)

  &.default
    background-color: $btn-default-color

  for $type in $color-types
    &.{$type}
      background-color: lookup('$tagsP-' + $type + '-color')

```

### 文件路径: `themes\butterfly\source\css\_tags\note.styl`
```styl
.note
  $note-icons = hexo-config('note.icons')
  position: relative
  margin: 0 0 20px
  padding: 15px

  if hexo-config('note.border_radius') is a 'unit'
    border-radius: unit(hexo-config('note.border_radius'), px)

  &.icon-padding
    padding-left: 3em

  & > .note-icon
    position: absolute
    top: calc(50% - .5em)
    left: .8em
    font-size: larger

  for $type in $color-types
    &.{$type}
      &:not(.disabled)
        border-left-color: lookup('$tagsP-' + $type + '-color') !important

        &.modern
          border-left-color: transparent !important
          color: lookup('$tagsP-' + $type + '-color')

        &:not(.simple)
          background: lighten(lookup('$tagsP-' + $type + '-color'), 85%) !important

      & > .note-icon
        color: lookup('$tagsP-' + $type + '-color')

  &.simple
    border: 1px solid #EEEEEE
    border-left-width: 5px

  &.modern
    border: 1px solid transparent !important
    background-color: #f5f5f5
    color: $font-black

  &.flat
    border: initial
    border-left: 5px solid #EEEEEE
    background-color: lighten(#EEEEEE, 65%)
    color: $font-black

  h2,
  h3,
  h4,
  h5,
  h6
    if $note-icons
      margin-top: 3px
    else
      margin-top: 0

    margin-bottom: 0
    padding-top: 0 !important
    border-bottom: initial

  p,
  ul,
  ol,
  table,
  pre,
  blockquote,
  img
    &:first-child
      margin-top: 0 !important

    &:last-child
      margin-bottom: 0 !important

  .img-alt
    margin: 5px 0 10px

  if $note-icons
    &:not(.no-icon)
      padding-left: 3em

      &::before
        position: absolute
        top: calc(50% - .95em)
        left: .8em
        font-size: larger
        @extend .fontawesomeIcon

  for $type in $note-types
    &.{$type}
      &.flat
        background: lookup('$note-' + $type + '-bg')

      &.modern
        border-color: lookup('$note-modern-' + $type + '-border')
        background: lookup('$note-modern-' + $type + '-bg')
        color: lookup('$note-modern-' + $type + '-text')

        a
          &:not(.btn)
            color: lookup('$note-modern-' + $type + '-text')

            &:hover
              color: lookup('$note-modern-' + $type + '-hover')

      &:not(.modern)
        border-left-color: lookup('$note-' + $type + '-border')

        h2,
        h3,
        h4,
        h5,
        h6
          color: lookup('$note-' + $type + '-text')

      if $note-icons
        &:not(.no-icon)
          &::before
            content: lookup('$note-' + $type + '-icon')

          &:not(.modern)
            &::before
              color: lookup('$note-' + $type + '-text')

```

### 文件路径: `themes\butterfly\source\css\_tags\series.styl`
```styl
.container
  .series-items
    a
      &:hover
        color: var(--pseudo-hover)
```

### 文件路径: `themes\butterfly\source\css\_tags\tabs.styl`
```styl

.container
  .tabs
    position: relative
    margin: 0 0 20px
    border-right: 1px solid var(--tab-border-color)
    border-bottom: 1px solid var(--tab-border-color)
    border-left: 1px solid var(--tab-border-color)
    addBorderRadius()
    overflow: hidden

    > .nav-tabs
      display: flex
      flex-wrap: wrap
      margin: 0
      padding: 0
      background: var(--tab-botton-bg)

      > .tab
        flex-grow: 1
        padding: 8px 18px
        border-top: 2px solid var(--tab-border-color)
        background: var(--tab-botton-bg)
        color: var(--tab-botton-color)
        line-height: 2
        transition: all .4s

        i
          width: 1.5em

        &.active
          border-top: 2px solid $tab-active-border-color
          background: var(--tab-button-active-bg)
          cursor: default

        &:not(.active)
          &:hover
            border-top: 2px solid var(--tab-button-hover-bg)
            background: var(--tab-button-hover-bg)

      &.no-default
        & ~ .tab-to-top
          display: none

    > .tab-contents
      .tab-item-content
        position: relative
        display: none
        padding: 36px 24px 10px

        +maxWidth768()
          padding: 24px 14px

        &.active
          display: block
          animation: tabshow .5s

        > :last-child
          margin-bottom: 0

    > .tab-to-top
      padding: 0 16px 10px 0
      width: 100%
      text-align: right

      button
        color: $tab-to-top-color

        &:hover
          color: $tab-to-top-hover-color

@keyframes tabshow
  0%
    transform: translateY(15px)

  100%
    transform: translateY(0)

```

### 文件路径: `themes\butterfly\source\css\_tags\timeline.styl`
```styl
.container
  .timeline
    margin: 0 10px 20px
    padding: 14px 0 5px 20px
    border-left: 2px solid var(--timeline-color, $theme-color)

    for $type in $color-types
      &.{$type}
        --timeline-color: lookup('$tagsP-' + $type + '-color')
        --timeline-bg: s('rgba(%s,%s,%s, 0.2)', red(lookup('$tagsP-' + $type + '-color')), green(lookup('$tagsP-' + $type + '-color')), blue(lookup('$tagsP-' + $type + '-color')))

    .timeline-item
      margin: 0 0 15px

      &:hover
        .item-circle
          &:before
            border-color: var(--timeline-color, $theme-color)

      &.headline
        .timeline-item-title
          .item-circle
            > p
              font-weight: 600
              font-size: 1.2em

            &:before
              left: -28px
              border: 4px solid var(--timeline-color, $theme-color)

        &:hover
          .item-circle
            &:before
              border-color: var(--pseudo-hover)

      .timeline-item-title
        position: relative

      .item-circle
        &:before
          position: absolute
          top: 50%
          left: -27px
          width: 6px
          height: 6px
          border: 3px solid var(--pseudo-hover)
          border-radius: 50%
          background: var(--card-bg)
          content: ''
          transition: all .3s
          transform: translate(0, -50%)

        > p
          margin: 0 0 8px
          font-weight: 500

      .timeline-item-content
        position: relative
        padding: 12px 15px
        border-radius: 8px
        background: var(--timeline-bg, lighten($theme-color, 85%))
        font-size: .93em

        & > :last-child
          margin-bottom: 0

    & + .timeline
      margin-top: -20px
```

### 文件路径: `themes\butterfly\source\css\_third-party\normalize.min.css`
```css
/*! normalize.css v8.0.1 | MIT License | github.com/necolas/normalize.css */
html {
  line-height: 1.15;
  -webkit-text-size-adjust: 100%
}

body {
  margin: 0
}

main {
  display: block
}

h1 {
  font-size: 2em;
  margin: .67em 0
}

hr {
  box-sizing: content-box;
  height: 0;
  overflow: visible
}

pre {
  font-family: monospace, monospace;
  font-size: 1em
}

a {
  background-color: transparent
}

abbr[title] {
  border-bottom: none;
  text-decoration: underline;
  text-decoration: underline dotted
}

b,
strong {
  font-weight: bolder
}

code,
kbd,
samp {
  font-family: monospace, monospace;
  font-size: 1em
}

small {
  font-size: 80%
}

sub,
sup {
  font-size: 75%;
  line-height: 0;
  position: relative;
  vertical-align: baseline
}

sub {
  bottom: -.25em
}

sup {
  top: -.5em
}

img {
  border-style: none
}

button,
input,
optgroup,
select,
textarea {
  font-family: inherit;
  font-size: 100%;
  line-height: 1.15;
  margin: 0
}

button,
input {
  overflow: visible
}

button,
select {
  text-transform: none
}

[type=button],
[type=reset],
[type=submit],
button {
  -webkit-appearance: button
}

[type=button]::-moz-focus-inner,
[type=reset]::-moz-focus-inner,
[type=submit]::-moz-focus-inner,
button::-moz-focus-inner {
  border-style: none;
  padding: 0
}

[type=button]:-moz-focusring,
[type=reset]:-moz-focusring,
[type=submit]:-moz-focusring,
button:-moz-focusring {
  outline: 1px dotted ButtonText
}

fieldset {
  padding: .35em .75em .625em
}

legend {
  box-sizing: border-box;
  color: inherit;
  display: table;
  max-width: 100%;
  padding: 0;
  white-space: normal
}

progress {
  vertical-align: baseline
}

textarea {
  overflow: auto
}

[type=checkbox],
[type=radio] {
  box-sizing: border-box;
  padding: 0
}

[type=number]::-webkit-inner-spin-button,
[type=number]::-webkit-outer-spin-button {
  height: auto
}

[type=search] {
  -webkit-appearance: textfield;
  outline-offset: -2px
}

[type=search]::-webkit-search-decoration {
  -webkit-appearance: none
}

::-webkit-file-upload-button {
  -webkit-appearance: button;
  font: inherit
}

details {
  display: block
}

summary {
  display: list-item
}

template {
  display: none
}

[hidden] {
  display: none
}
```

### 文件路径: `themes\butterfly\source\js\main.js`
```js
document.addEventListener('DOMContentLoaded', () => {
  let headerContentWidth, $nav
  let mobileSidebarOpen = false

  const adjustMenu = init => {
    const getAllWidth = ele => Array.from(ele).reduce((width, i) => width + i.offsetWidth, 0)

    if (init) {
      const blogInfoWidth = getAllWidth(document.querySelector('#blog-info > a').children)
      const menusWidth = getAllWidth(document.getElementById('menus').children)
      headerContentWidth = blogInfoWidth + menusWidth
      $nav = document.getElementById('nav')
    }

    const hideMenuIndex = window.innerWidth <= 768 || headerContentWidth > $nav.offsetWidth - 120
    $nav.classList.toggle('hide-menu', hideMenuIndex)
  }

  // 初始化header
  const initAdjust = () => {
    adjustMenu(true)
    $nav.classList.add('show')
  }

  // sidebar menus
  const sidebarFn = {
    open: () => {
      btf.overflowPaddingR.add()
      btf.animateIn(document.getElementById('menu-mask'), 'to_show 0.5s')
      document.getElementById('sidebar-menus').classList.add('open')
      mobileSidebarOpen = true
    },
    close: () => {
      btf.overflowPaddingR.remove()
      btf.animateOut(document.getElementById('menu-mask'), 'to_hide 0.5s')
      document.getElementById('sidebar-menus').classList.remove('open')
      mobileSidebarOpen = false
    }
  }

  /**
   * 首頁top_img底下的箭頭
   */
  const scrollDownInIndex = () => {
    const handleScrollToDest = () => {
      btf.scrollToDest(document.getElementById('content-inner').offsetTop, 300)
    }

    const $scrollDownEle = document.getElementById('scroll-down')
    $scrollDownEle && btf.addEventListenerPjax($scrollDownEle, 'click', handleScrollToDest)
  }

  /**
   * 代碼
   * 只適用於Hexo默認的代碼渲染
   */
  const addHighlightTool = () => {
    const highLight = GLOBAL_CONFIG.highlight
    if (!highLight) return

    const { highlightCopy, highlightLang, highlightHeightLimit, highlightFullpage, highlightMacStyle, plugin } = highLight
    const isHighlightShrink = GLOBAL_CONFIG_SITE.isHighlightShrink
    const isShowTool = highlightCopy || highlightLang || isHighlightShrink !== undefined || highlightFullpage || highlightMacStyle
    const $figureHighlight = plugin === 'highlight.js' ? document.querySelectorAll('figure.highlight') : document.querySelectorAll('pre[class*="language-"]')

    if (!((isShowTool || highlightHeightLimit) && $figureHighlight.length)) return

    const isPrismjs = plugin === 'prismjs'
    const highlightShrinkClass = isHighlightShrink === true ? 'closed' : ''
    const highlightShrinkEle = isHighlightShrink !== undefined ? '<i class="fas fa-angle-down expand"></i>' : ''
    const highlightCopyEle = highlightCopy ? '<div class="copy-notice"></div><i class="fas fa-paste copy-button"></i>' : ''
    const highlightMacStyleEle = '<div class="macStyle"><div class="mac-close"></div><div class="mac-minimize"></div><div class="mac-maximize"></div></div>'
    const highlightFullpageEle = highlightFullpage ? '<i class="fa-solid fa-up-right-and-down-left-from-center fullpage-button"></i>' : ''

    const alertInfo = (ele, text) => {
      if (GLOBAL_CONFIG.Snackbar !== undefined) {
        btf.snackbarShow(text)
      } else {
        ele.textContent = text
        ele.style.opacity = 1
        setTimeout(() => { ele.style.opacity = 0 }, 800)
      }
    }

    const copy = async (text, ctx) => {
      try {
        await navigator.clipboard.writeText(text)
        alertInfo(ctx, GLOBAL_CONFIG.copy.success)
      } catch (err) {
        console.error('Failed to copy: ', err)
        alertInfo(ctx, GLOBAL_CONFIG.copy.noSupport)
      }
    }

    // click events
    const highlightCopyFn = (ele, clickEle) => {
      const $buttonParent = ele.parentNode
      $buttonParent.classList.add('copy-true')
      const preCodeSelector = isPrismjs ? 'pre code' : 'table .code pre'
      const codeElement = $buttonParent.querySelector(preCodeSelector)
      if (!codeElement) return
      copy(codeElement.innerText, clickEle.previousElementSibling)
      $buttonParent.classList.remove('copy-true')
    }

    const highlightShrinkFn = ele => ele.classList.toggle('closed')

    const codeFullpage = (item, clickEle) => {
      const wrapEle = item.closest('figure.highlight')
      const isFullpage = wrapEle.classList.toggle('code-fullpage')

      document.body.style.overflow = isFullpage ? 'hidden' : ''
      clickEle.classList.toggle('fa-down-left-and-up-right-to-center', isFullpage)
      clickEle.classList.toggle('fa-up-right-and-down-left-from-center', !isFullpage)
    }

    const highlightToolsFn = e => {
      const $target = e.target.classList
      const currentElement = e.currentTarget
      if ($target.contains('expand')) highlightShrinkFn(currentElement)
      else if ($target.contains('copy-button')) highlightCopyFn(currentElement, e.target)
      else if ($target.contains('fullpage-button')) codeFullpage(currentElement, e.target)
    }

    const expandCode = e => e.currentTarget.classList.toggle('expand-done')

    // 獲取隱藏狀態下元素的真實高度
    const getActualHeight = item => {
      const hiddenElements = new Map()

      const fix = () => {
        let current = item
        while (current !== document.body && current != null) {
          if (window.getComputedStyle(current).display === 'none') {
            hiddenElements.set(current, current.getAttribute('style') || '')
          }
          current = current.parentNode
        }

        const style = 'visibility: hidden !important; display: block !important;'
        hiddenElements.forEach((originalStyle, elem) => {
          elem.setAttribute('style', originalStyle ? originalStyle + ';' + style : style)
        })
      }

      const restore = () => {
        hiddenElements.forEach((originalStyle, elem) => {
          if (originalStyle === '') elem.removeAttribute('style')
          else elem.setAttribute('style', originalStyle)
        })
      }

      fix()
      const height = item.offsetHeight
      restore()
      return height
    }

    const createEle = (lang, item) => {
      const fragment = document.createDocumentFragment()

      if (isShowTool) {
        const hlTools = document.createElement('div')
        hlTools.className = `highlight-tools ${highlightShrinkClass}`
        hlTools.innerHTML = highlightMacStyleEle + highlightShrinkEle + lang + highlightCopyEle + highlightFullpageEle
        btf.addEventListenerPjax(hlTools, 'click', highlightToolsFn)
        fragment.appendChild(hlTools)
      }

      if (highlightHeightLimit && getActualHeight(item) > highlightHeightLimit + 30) {
        const ele = document.createElement('div')
        ele.className = 'code-expand-btn'
        ele.innerHTML = '<i class="fas fa-angle-double-down"></i>'
        btf.addEventListenerPjax(ele, 'click', expandCode)
        fragment.appendChild(ele)
      }

      isPrismjs ? item.parentNode.insertBefore(fragment, item) : item.insertBefore(fragment, item.firstChild)
    }

    $figureHighlight.forEach(item => {
      let langName = ''
      if (isPrismjs) btf.wrap(item, 'figure', { class: 'highlight' })

      if (!highlightLang) {
        createEle('', item)
        return
      }

      if (isPrismjs) {
        langName = item.getAttribute('data-language') || 'Code'
      } else {
        langName = item.getAttribute('class').split(' ')[1]
        if (langName === 'plain' || langName === undefined) langName = 'Code'
      }
      createEle(`<div class="code-lang">${langName}</div>`, item)
    })
  }

  /**
   * PhotoFigcaption
   */
  const addPhotoFigcaption = () => {
    if (!GLOBAL_CONFIG.isPhotoFigcaption) return
    document.querySelectorAll('#article-container img').forEach(item => {
      const altValue = item.title || item.alt
      if (!altValue) return
      const ele = document.createElement('div')
      ele.className = 'img-alt text-center'
      ele.textContent = altValue
      item.insertAdjacentElement('afterend', ele)
    })
  }

  /**
   * Lightbox
   */
  const runLightbox = () => {
    btf.loadLightbox(document.querySelectorAll('#article-container img:not(.no-lightbox)'))
  }

  /**
   * justified-gallery 圖庫排版
   */

  const fetchUrl = async url => {
    try {
      const response = await fetch(url)
      return await response.json()
    } catch (error) {
      console.error('Failed to fetch URL:', error)
      return []
    }
  }

  const runJustifiedGallery = (container, data, config) => {
    const { isButton, limit, firstLimit, tabs } = config

    const dataLength = data.length
    const maxGroupKey = Math.ceil((dataLength - firstLimit) / limit + 1)

    // Gallery configuration
    const igConfig = {
      gap: 5,
      isConstantSize: true,
      sizeRange: [150, 600],
      // useResizeObserver: true,
      // observeChildren: true,
      useTransform: true
      // useRecycle: false
    }

    const ig = new InfiniteGrid.JustifiedInfiniteGrid(container, igConfig)
    let isLayoutHidden = false

    // Utility functions
    const sanitizeString = str => (str && str.replace(/"/g, '&quot;')) || ''

    const createImageItem = item => {
      const alt = item.alt ? `alt="${sanitizeString(item.alt)}"` : ''
      const title = item.title ? `title="${sanitizeString(item.title)}"` : ''
      return `<div class="item">
        <img src="${item.url}" data-grid-maintained-target="true" ${alt} ${title} />
      </div>`
    }

    const getItems = (nextGroupKey, count, isFirst = false) => {
      const startIndex = isFirst ? (nextGroupKey - 1) * count : (nextGroupKey - 2) * count + firstLimit
      return data.slice(startIndex, startIndex + count).map(createImageItem)
    }

    // Load more button
    const addLoadMoreButton = container => {
      const button = document.createElement('button')
      button.innerHTML = `${GLOBAL_CONFIG.infinitegrid.buttonText}<i class="fa-solid fa-arrow-down"></i>`

      button.addEventListener('click', () => {
        button.remove()
        btf.setLoading.add(container)
        appendItems(ig.getGroups().length + 1, limit)
      }, { once: true })

      container.insertAdjacentElement('afterend', button)
    }

    const appendItems = (nextGroupKey, count, isFirst) => {
      ig.append(getItems(nextGroupKey, count, isFirst), nextGroupKey)
    }

    // Event handlers
    const handleRenderComplete = e => {
      if (tabs) {
        const parentNode = container.parentNode
        if (isLayoutHidden) {
          parentNode.style.visibility = 'visible'
        }
        if (container.offsetHeight === 0) {
          parentNode.style.visibility = 'hidden'
          isLayoutHidden = true
        }
      }

      const { updated, isResize, mounted } = e
      if (!updated.length || !mounted.length || isResize) return

      btf.loadLightbox(container.querySelectorAll('img:not(.medium-zoom-image)'))

      if (ig.getGroups().length === maxGroupKey) {
        btf.setLoading.remove(container)
        !tabs && ig.off('renderComplete', handleRenderComplete)
        return
      }

      if (isButton) {
        btf.setLoading.remove(container)
        addLoadMoreButton(container)
      }
    }

    const handleRequestAppend = btf.debounce(e => {
      const nextGroupKey = (+e.groupKey || 0) + 1

      if (nextGroupKey === 1) appendItems(nextGroupKey, firstLimit, true)
      else appendItems(nextGroupKey, limit)

      if (nextGroupKey === maxGroupKey) ig.off('requestAppend', handleRequestAppend)
    }, 300)

    btf.setLoading.add(container)
    ig.on('renderComplete', handleRenderComplete)

    if (isButton) {
      appendItems(1, firstLimit, true)
    } else {
      ig.on('requestAppend', handleRequestAppend)
      ig.renderItems()
    }

    btf.addGlobalFn('pjaxSendOnce', () => ig.destroy())
  }

  const addJustifiedGallery = async (elements, tabs = false) => {
    if (!elements.length) return

    const initGallery = async () => {
      for (const element of elements) {
        if (btf.isHidden(element) || element.classList.contains('loaded')) continue

        const config = {
          isButton: element.getAttribute('data-button') === 'true',
          limit: parseInt(element.getAttribute('data-limit'), 10),
          firstLimit: parseInt(element.getAttribute('data-first'), 10),
          tabs
        }

        const container = element.firstElementChild
        const content = container.textContent
        container.textContent = ''
        element.classList.add('loaded')

        try {
          const data = element.getAttribute('data-type') === 'url' ? await fetchUrl(content) : JSON.parse(content)
          runJustifiedGallery(container, data, config)
        } catch (error) {
          console.error('Gallery data parsing failed:', error)
        }
      }
    }

    if (typeof InfiniteGrid === 'function') {
      await initGallery()
    } else {
      await btf.getScript(GLOBAL_CONFIG.infinitegrid.js)
      await initGallery()
    }
  }

  /**
   * rightside scroll percent
   */
  const rightsideScrollPercent = currentTop => {
    const scrollPercent = btf.getScrollPercent(currentTop, document.body)
    const goUpElement = document.getElementById('go-up')

    if (scrollPercent < 95) {
      goUpElement.classList.add('show-percent')
      goUpElement.querySelector('.scroll-percent').textContent = scrollPercent
    } else {
      goUpElement.classList.remove('show-percent')
    }
  }

  /**
   * 滾動處理
   */
  const scrollFn = () => {
    const $rightside = document.getElementById('rightside')
    const innerHeight = window.innerHeight + 56
    let initTop = 0
    const $header = document.getElementById('page-header')
    const isChatBtn = typeof chatBtn !== 'undefined'
    const isShowPercent = GLOBAL_CONFIG.percent.rightside

    // 檢查文檔高度是否小於視窗高度
    const checkDocumentHeight = () => {
      if (document.body.scrollHeight <= innerHeight) {
        $rightside.classList.add('rightside-show')
        return true
      }
      return false
    }

    // 如果文檔高度小於視窗高度,直接返回
    if (checkDocumentHeight()) return

    // find the scroll direction
    const scrollDirection = currentTop => {
      const result = currentTop > initTop // true is down & false is up
      initTop = currentTop
      return result
    }

    let flag = ''
    const scrollTask = btf.throttle(() => {
      const currentTop = window.scrollY || document.documentElement.scrollTop
      const isDown = scrollDirection(currentTop)
      if (currentTop > 56) {
        if (flag === '') {
          $header.classList.add('nav-fixed')
          $rightside.classList.add('rightside-show')
        }

        if (isDown) {
          if (flag !== 'down') {
            $header.classList.remove('nav-visible')
            isChatBtn && window.chatBtn.hide()
            flag = 'down'
          }
        } else {
          if (flag !== 'up') {
            $header.classList.add('nav-visible')
            isChatBtn && window.chatBtn.show()
            flag = 'up'
          }
        }
      } else {
        flag = ''
        if (currentTop === 0) {
          $header.classList.remove('nav-fixed', 'nav-visible')
        }
        $rightside.classList.remove('rightside-show')
      }

      isShowPercent && rightsideScrollPercent(currentTop)
      checkDocumentHeight()
    }, 300)

    btf.addEventListenerPjax(window, 'scroll', scrollTask, { passive: true })
  }

  /**
  * toc,anchor
  */
  const scrollFnToDo = () => {
    const isToc = GLOBAL_CONFIG_SITE.isToc
    const isAnchor = GLOBAL_CONFIG.isAnchor
    const $article = document.getElementById('article-container')

    if (!($article && (isToc || isAnchor))) return

    let $tocLink, $cardToc, autoScrollToc, $tocPercentage, isExpand

    if (isToc) {
      const $cardTocLayout = document.getElementById('card-toc')
      $cardToc = $cardTocLayout.querySelector('.toc-content')
      $tocLink = $cardToc.querySelectorAll('.toc-link')
      $tocPercentage = $cardTocLayout.querySelector('.toc-percentage')
      isExpand = $cardToc.classList.contains('is-expand')

      // toc元素點擊
      const tocItemClickFn = e => {
        const target = e.target.closest('.toc-link')
        if (!target) return

        e.preventDefault()
        btf.scrollToDest(btf.getEleTop(document.getElementById(decodeURI(target.getAttribute('href')).replace('#', ''))), 300)
        if (window.innerWidth < 900) {
          $cardTocLayout.classList.remove('open')
        }
      }

      btf.addEventListenerPjax($cardToc, 'click', tocItemClickFn)

      autoScrollToc = item => {
        const sidebarHeight = $cardToc.clientHeight
        const itemOffsetTop = item.offsetTop
        const itemHeight = item.clientHeight
        const scrollTop = $cardToc.scrollTop
        const offset = itemOffsetTop - scrollTop
        const middlePosition = (sidebarHeight - itemHeight) / 2

        if (offset !== middlePosition) {
          $cardToc.scrollTop = scrollTop + (offset - middlePosition)
        }
      }

      // 處理 hexo-blog-encrypt 事件
      $cardToc.style.display = 'block'
    }

    // find head position & add active class
    const $articleList = $article.querySelectorAll('h1,h2,h3,h4,h5,h6')
    let detectItem = ''

    const findHeadPosition = top => {
      if (top === 0) return false

      let currentId = ''
      let currentIndex = ''

      for (let i = 0; i < $articleList.length; i++) {
        const ele = $articleList[i]
        if (top > btf.getEleTop(ele) - 80) {
          const id = ele.id
          currentId = id ? '#' + encodeURI(id) : ''
          currentIndex = i
        } else {
          break
        }
      }

      if (detectItem === currentIndex) return

      if (isAnchor) btf.updateAnchor(currentId)

      detectItem = currentIndex

      if (isToc) {
        $cardToc.querySelectorAll('.active').forEach(i => i.classList.remove('active'))

        if (currentId) {
          const currentActive = $tocLink[currentIndex]
          currentActive.classList.add('active')

          setTimeout(() => autoScrollToc(currentActive), 0)

          if (!isExpand) {
            let parent = currentActive.parentNode
            while (!parent.matches('.toc')) {
              if (parent.matches('li')) parent.classList.add('active')
              parent = parent.parentNode
            }
          }
        }
      }
    }

    // main of scroll
    const tocScrollFn = btf.throttle(() => {
      const currentTop = window.scrollY || document.documentElement.scrollTop
      if (isToc && GLOBAL_CONFIG.percent.toc) {
        $tocPercentage.textContent = btf.getScrollPercent(currentTop, $article)
      }
      findHeadPosition(currentTop)
    }, 100)

    btf.addEventListenerPjax(window, 'scroll', tocScrollFn, { passive: true })
  }

  const handleThemeChange = mode => {
    const globalFn = window.globalFn || {}
    const themeChange = globalFn.themeChange || {}
    if (!themeChange) {
      return
    }

    Object.keys(themeChange).forEach(key => {
      const themeChangeFn = themeChange[key]
      if (['disqus', 'disqusjs'].includes(key)) {
        setTimeout(() => themeChangeFn(mode), 300)
      } else {
        themeChangeFn(mode)
      }
    })
  }

  /**
   * Rightside
   */
  const rightSideFn = {
    readmode: () => { // read mode
      const $body = document.body
      const newEle = document.createElement('button')

      const exitReadMode = () => {
        $body.classList.remove('read-mode')
        newEle.remove()
        newEle.removeEventListener('click', exitReadMode)
      }

      $body.classList.add('read-mode')
      newEle.type = 'button'
      newEle.className = 'fas fa-sign-out-alt exit-readmode'
      newEle.addEventListener('click', exitReadMode)
      $body.appendChild(newEle)
    },
    darkmode: () => { // switch between light and dark mode
      const willChangeMode = document.documentElement.getAttribute('data-theme') === 'dark' ? 'light' : 'dark'
      if (willChangeMode === 'dark') {
        btf.activateDarkMode()
        GLOBAL_CONFIG.Snackbar !== undefined && btf.snackbarShow(GLOBAL_CONFIG.Snackbar.day_to_night)
      } else {
        btf.activateLightMode()
        GLOBAL_CONFIG.Snackbar !== undefined && btf.snackbarShow(GLOBAL_CONFIG.Snackbar.night_to_day)
      }
      btf.saveToLocal.set('theme', willChangeMode, 2)
      handleThemeChange(willChangeMode)
    },
    'rightside-config': item => { // Show or hide rightside-hide-btn
      const hideLayout = item.firstElementChild
      if (hideLayout.classList.contains('show')) {
        hideLayout.classList.add('status')
        setTimeout(() => {
          hideLayout.classList.remove('status')
        }, 300)
      }

      hideLayout.classList.toggle('show')
    },
    'go-up': () => { // Back to top
      btf.scrollToDest(0, 500)
    },
    'hide-aside-btn': () => { // Hide aside
      const $htmlDom = document.documentElement.classList
      const saveStatus = $htmlDom.contains('hide-aside') ? 'show' : 'hide'
      btf.saveToLocal.set('aside-status', saveStatus, 2)
      $htmlDom.toggle('hide-aside')
    },
    'mobile-toc-button': (p, item) => { // Show mobile toc
      const tocEle = document.getElementById('card-toc')
      tocEle.style.transition = 'transform 0.3s ease-in-out'

      const tocEleHeight = tocEle.clientHeight
      const btData = item.getBoundingClientRect()

      const tocEleBottom = window.innerHeight - btData.bottom - 30
      if (tocEleHeight > tocEleBottom) {
        tocEle.style.transformOrigin = `right ${tocEleHeight - tocEleBottom - btData.height / 2}px`
      }

      tocEle.classList.toggle('open')
      tocEle.addEventListener('transitionend', () => {
        tocEle.style.cssText = ''
      }, { once: true })
    },
    'chat-btn': () => { // Show chat
      window.chatBtnFn()
    },
    translateLink: () => { // switch between traditional and simplified chinese
      window.translateFn.translatePage()
    }
  }

  document.getElementById('rightside').addEventListener('click', e => {
    const $target = e.target.closest('[id]')
    if ($target && rightSideFn[$target.id]) {
      rightSideFn[$target.id](e.currentTarget, $target)
    }
  })

  /**
   * menu
   * 側邊欄sub-menu 展開/收縮
   */
  const clickFnOfSubMenu = () => {
    const handleClickOfSubMenu = e => {
      const target = e.target.closest('.site-page.group')
      if (!target) return
      target.classList.toggle('hide')
    }

    const menusItems = document.querySelector('#sidebar-menus .menus_items')
    menusItems && menusItems.addEventListener('click', handleClickOfSubMenu)
  }

  /**
   * 手机端目录点击
   */
  const openMobileMenu = () => {
    const toggleMenu = document.getElementById('toggle-menu')
    if (!toggleMenu) return
    btf.addEventListenerPjax(toggleMenu, 'click', () => { sidebarFn.open() })
  }

  /**
 * 複製時加上版權信息
 */
  const addCopyright = () => {
    const { limitCount, languages } = GLOBAL_CONFIG.copyright

    const handleCopy = (e) => {
      e.preventDefault()
      const copyFont = window.getSelection(0).toString()
      let textFont = copyFont
      if (copyFont.length > limitCount) {
        textFont = `${copyFont}\n\n\n${languages.author}\n${languages.link}${window.location.href}\n${languages.source}\n${languages.info}`
      }
      if (e.clipboardData) {
        return e.clipboardData.setData('text', textFont)
      } else {
        return window.clipboardData.setData('text', textFont)
      }
    }

    document.body.addEventListener('copy', handleCopy)
  }

  /**
   * 網頁運行時間
   */
  const addRuntime = () => {
    const $runtimeCount = document.getElementById('runtimeshow')
    if ($runtimeCount) {
      const publishDate = $runtimeCount.getAttribute('data-publishDate')
      $runtimeCount.textContent = `${btf.diffDate(publishDate)} ${GLOBAL_CONFIG.runtime}`
    }
  }

  /**
   * 最後一次更新時間
   */
  const addLastPushDate = () => {
    const $lastPushDateItem = document.getElementById('last-push-date')
    if ($lastPushDateItem) {
      const lastPushDate = $lastPushDateItem.getAttribute('data-lastPushDate')
      $lastPushDateItem.textContent = btf.diffDate(lastPushDate, true)
    }
  }

  /**
   * table overflow
   */
  const addTableWrap = () => {
    const $table = document.querySelectorAll('#article-container table')
    if (!$table.length) return

    $table.forEach(item => {
      if (!item.closest('.highlight')) {
        btf.wrap(item, 'div', { class: 'table-wrap' })
      }
    })
  }

  /**
   * tag-hide
   */
  const clickFnOfTagHide = () => {
    const hideButtons = document.querySelectorAll('#article-container .hide-button')
    if (!hideButtons.length) return
    hideButtons.forEach(item => item.addEventListener('click', e => {
      const currentTarget = e.currentTarget
      currentTarget.classList.add('open')
      addJustifiedGallery(currentTarget.nextElementSibling.querySelectorAll('.gallery-container'))
    }, { once: true }))
  }

  const tabsFn = () => {
    const navTabsElements = document.querySelectorAll('#article-container .tabs')
    if (!navTabsElements.length) return

    const setActiveClass = (elements, activeIndex) => {
      elements.forEach((el, index) => {
        el.classList.toggle('active', index === activeIndex)
      })
    }

    const handleNavClick = e => {
      const target = e.target.closest('button')
      if (!target || target.classList.contains('active')) return

      const navItems = [...e.currentTarget.children]
      const tabContents = [...e.currentTarget.nextElementSibling.children]
      const indexOfButton = navItems.indexOf(target)
      setActiveClass(navItems, indexOfButton)
      e.currentTarget.classList.remove('no-default')
      setActiveClass(tabContents, indexOfButton)
      addJustifiedGallery(tabContents[indexOfButton].querySelectorAll('.gallery-container'), true)
    }

    const handleToTopClick = tabElement => e => {
      if (e.target.closest('button')) {
        btf.scrollToDest(btf.getEleTop(tabElement), 300)
      }
    }

    navTabsElements.forEach(tabElement => {
      btf.addEventListenerPjax(tabElement.firstElementChild, 'click', handleNavClick)
      btf.addEventListenerPjax(tabElement.lastElementChild, 'click', handleToTopClick(tabElement))
    })
  }

  const toggleCardCategory = () => {
    const cardCategory = document.querySelector('#aside-cat-list.expandBtn')
    if (!cardCategory) return

    const handleToggleBtn = e => {
      const target = e.target
      if (target.nodeName === 'I') {
        e.preventDefault()
        target.parentNode.classList.toggle('expand')
      }
    }
    btf.addEventListenerPjax(cardCategory, 'click', handleToggleBtn, true)
  }

  const addPostOutdateNotice = () => {
    const ele = document.getElementById('post-outdate-notice')
    if (!ele) return

    const { limitDay, messagePrev, messageNext, postUpdate } = JSON.parse(ele.getAttribute('data'))
    const diffDay = btf.diffDate(postUpdate)
    if (diffDay >= limitDay) {
      ele.textContent = `${messagePrev} ${diffDay} ${messageNext}`
      ele.hidden = false
    }
  }

  const lazyloadImg = () => {
    window.lazyLoadInstance = new LazyLoad({
      elements_selector: 'img',
      threshold: 0,
      data_src: 'lazy-src'
    })

    btf.addGlobalFn('pjaxComplete', () => {
      window.lazyLoadInstance.update()
    }, 'lazyload')
  }

  const relativeDate = selector => {
    selector.forEach(item => {
      item.textContent = btf.diffDate(item.getAttribute('datetime'), true)
      item.style.display = 'inline'
    })
  }

  const justifiedIndexPostUI = () => {
    const recentPostsElement = document.getElementById('recent-posts')
    if (!(recentPostsElement && recentPostsElement.classList.contains('masonry'))) return

    const init = () => {
      const masonryItem = new InfiniteGrid.MasonryInfiniteGrid('.recent-post-items', {
        gap: { horizontal: 10, vertical: 20 },
        useTransform: true,
        useResizeObserver: true
      })
      masonryItem.renderItems()
      btf.addGlobalFn('pjaxCompleteOnce', () => { masonryItem.destroy() }, 'removeJustifiedIndexPostUI')
    }

    typeof InfiniteGrid === 'function' ? init() : btf.getScript(`${GLOBAL_CONFIG.infinitegrid.js}`).then(init)
  }

  const unRefreshFn = () => {
    window.addEventListener('resize', () => {
      adjustMenu(false)
      mobileSidebarOpen && btf.isHidden(document.getElementById('toggle-menu')) && sidebarFn.close()
    })

    const menuMask = document.getElementById('menu-mask')
    menuMask && menuMask.addEventListener('click', () => { sidebarFn.close() })

    clickFnOfSubMenu()
    GLOBAL_CONFIG.islazyloadPlugin && lazyloadImg()
    GLOBAL_CONFIG.copyright !== undefined && addCopyright()

    if (GLOBAL_CONFIG.autoDarkmode) {
      window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', e => {
        if (btf.saveToLocal.get('theme') !== undefined) return
        e.matches ? handleThemeChange('dark') : handleThemeChange('light')
      })
    }
  }

  const forPostFn = () => {
    addHighlightTool()
    addPhotoFigcaption()
    addJustifiedGallery(document.querySelectorAll('#article-container .gallery-container'))
    runLightbox()
    scrollFnToDo()
    addTableWrap()
    clickFnOfTagHide()
    tabsFn()
  }

  const refreshFn = () => {
    initAdjust()
    justifiedIndexPostUI()

    if (GLOBAL_CONFIG_SITE.pageType === 'post') {
      addPostOutdateNotice()
      GLOBAL_CONFIG.relativeDate.post && relativeDate(document.querySelectorAll('#post-meta time'))
    } else {
      GLOBAL_CONFIG.relativeDate.homepage && relativeDate(document.querySelectorAll('#recent-posts time'))
      GLOBAL_CONFIG.runtime && addRuntime()
      addLastPushDate()
      toggleCardCategory()
    }

    GLOBAL_CONFIG_SITE.pageType === 'home' && scrollDownInIndex()
    scrollFn()

    forPostFn()
    GLOBAL_CONFIG_SITE.pageType !== 'shuoshuo' && btf.switchComments(document)
    openMobileMenu()
  }

  btf.addGlobalFn('pjaxComplete', refreshFn, 'refreshFn')
  refreshFn()
  unRefreshFn()

  // 處理 hexo-blog-encrypt 事件
  window.addEventListener('hexo-blog-decrypt', e => {
    forPostFn()
    window.translateFn.translateInitialization()
    Object.values(window.globalFn.encrypt).forEach(fn => {
      fn()
    })
  })
})

```

### 文件路径: `themes\butterfly\source\js\tw_cn.js`
```js
document.addEventListener('DOMContentLoaded', () => {
  const { defaultEncoding, translateDelay, msgToTraditionalChinese, msgToSimplifiedChinese } = GLOBAL_CONFIG.translate
  const snackbarData = GLOBAL_CONFIG.Snackbar
  const targetEncodingCookie = 'translate-chn-cht'

  let currentEncoding = defaultEncoding
  let targetEncoding = Number(btf.saveToLocal.get(targetEncodingCookie)) || defaultEncoding
  const translateButtonObject = document.getElementById('translateLink')
  const isSnackbar = snackbarData !== undefined

  const setLang = () => {
    document.documentElement.lang = targetEncoding === 1 ? 'zh-TW' : 'zh-CN'
  }

  const translateText = (txt) => {
    if (!txt) return ''
    if (currentEncoding === 1 && targetEncoding === 2) return Simplized(txt)
    if (currentEncoding === 2 && targetEncoding === 1) return Traditionalized(txt)
    return txt
  }

  const translateBody = (fobj) => {
    const nodes = typeof fobj === 'object' ? fobj.childNodes : document.body.childNodes

    for (const node of nodes) {
      // Skip BR, HR tags, or the translate button object
      if (['BR', 'HR'].includes(node.tagName) || node === translateButtonObject) continue

      if (node.nodeType === Node.ELEMENT_NODE) {
        const { tagName, title, alt, placeholder, value, type } = node

        // Translate title, alt, placeholder
        if (title) node.title = translateText(title)
        if (alt) node.alt = translateText(alt)
        if (placeholder) node.placeholder = translateText(placeholder)

        // Translate input value except text and hidden types
        if (tagName === 'INPUT' && value && type !== 'text' && type !== 'hidden') {
          node.value = translateText(value)
        }

        // Recursively translate child nodes
        translateBody(node)
      } else if (node.nodeType === Node.TEXT_NODE) {
        // Translate text node data
        node.data = translateText(node.data)
      }
    }
  }

  const translatePage = () => {
    if (targetEncoding === 1) {
      currentEncoding = 1
      targetEncoding = 2
      translateButtonObject.textContent = msgToTraditionalChinese
      isSnackbar && btf.snackbarShow(snackbarData.cht_to_chs)
    } else if (targetEncoding === 2) {
      currentEncoding = 2
      targetEncoding = 1
      translateButtonObject.textContent = msgToSimplifiedChinese
      isSnackbar && btf.snackbarShow(snackbarData.chs_to_cht)
    }
    btf.saveToLocal.set(targetEncodingCookie, targetEncoding, 2)
    setLang()
    translateBody()
  }

  const JTPYStr = () => '万与丑专业丛东丝丢两严丧个丬丰临为丽举么义乌乐乔习乡书买乱争于亏云亘亚产亩亲亵亸亿仅从仑仓仪们价众优伙会伛伞伟传伤伥伦伧伪伫体余佣佥侠侣侥侦侧侨侩侪侬俣俦俨俩俪俭债倾偬偻偾偿傥傧储傩儿兑兖党兰关兴兹养兽冁内冈册写军农冢冯冲决况冻净凄凉凌减凑凛几凤凫凭凯击凼凿刍划刘则刚创删别刬刭刽刿剀剂剐剑剥剧劝办务劢动励劲劳势勋勐勚匀匦匮区医华协单卖卢卤卧卫却卺厂厅历厉压厌厍厕厢厣厦厨厩厮县参叆叇双发变叙叠叶号叹叽吁后吓吕吗吣吨听启吴呒呓呕呖呗员呙呛呜咏咔咙咛咝咤咴咸哌响哑哒哓哔哕哗哙哜哝哟唛唝唠唡唢唣唤唿啧啬啭啮啰啴啸喷喽喾嗫呵嗳嘘嘤嘱噜噼嚣嚯团园囱围囵国图圆圣圹场坂坏块坚坛坜坝坞坟坠垄垅垆垒垦垧垩垫垭垯垱垲垴埘埙埚埝埯堑堕塆墙壮声壳壶壸处备复够头夸夹夺奁奂奋奖奥妆妇妈妩妪妫姗姜娄娅娆娇娈娱娲娴婳婴婵婶媪嫒嫔嫱嬷孙学孪宁宝实宠审宪宫宽宾寝对寻导寿将尔尘尧尴尸尽层屃屉届属屡屦屿岁岂岖岗岘岙岚岛岭岳岽岿峃峄峡峣峤峥峦崂崃崄崭嵘嵚嵛嵝嵴巅巩巯币帅师帏帐帘帜带帧帮帱帻帼幂幞干并广庄庆庐庑库应庙庞废庼廪开异弃张弥弪弯弹强归当录彟彦彻径徕御忆忏忧忾怀态怂怃怄怅怆怜总怼怿恋恳恶恸恹恺恻恼恽悦悫悬悭悯惊惧惨惩惫惬惭惮惯愍愠愤愦愿慑慭憷懑懒懔戆戋戏戗战戬户扎扑扦执扩扪扫扬扰抚抛抟抠抡抢护报担拟拢拣拥拦拧拨择挂挚挛挜挝挞挟挠挡挢挣挤挥挦捞损捡换捣据捻掳掴掷掸掺掼揸揽揿搀搁搂搅携摄摅摆摇摈摊撄撑撵撷撸撺擞攒敌敛数斋斓斗斩断无旧时旷旸昙昼昽显晋晒晓晔晕晖暂暧札术朴机杀杂权条来杨杩杰极构枞枢枣枥枧枨枪枫枭柜柠柽栀栅标栈栉栊栋栌栎栏树栖样栾桊桠桡桢档桤桥桦桧桨桩梦梼梾检棂椁椟椠椤椭楼榄榇榈榉槚槛槟槠横樯樱橥橱橹橼檐檩欢欤欧歼殁殇残殒殓殚殡殴毁毂毕毙毡毵氇气氢氩氲汇汉污汤汹沓沟没沣沤沥沦沧沨沩沪沵泞泪泶泷泸泺泻泼泽泾洁洒洼浃浅浆浇浈浉浊测浍济浏浐浑浒浓浔浕涂涌涛涝涞涟涠涡涢涣涤润涧涨涩淀渊渌渍渎渐渑渔渖渗温游湾湿溃溅溆溇滗滚滞滟滠满滢滤滥滦滨滩滪漤潆潇潋潍潜潴澜濑濒灏灭灯灵灾灿炀炉炖炜炝点炼炽烁烂烃烛烟烦烧烨烩烫烬热焕焖焘煅煳熘爱爷牍牦牵牺犊犟状犷犸犹狈狍狝狞独狭狮狯狰狱狲猃猎猕猡猪猫猬献獭玑玙玚玛玮环现玱玺珉珏珐珑珰珲琎琏琐琼瑶瑷璇璎瓒瓮瓯电画畅畲畴疖疗疟疠疡疬疮疯疱疴痈痉痒痖痨痪痫痴瘅瘆瘗瘘瘪瘫瘾瘿癞癣癫癯皑皱皲盏盐监盖盗盘眍眦眬着睁睐睑瞒瞩矫矶矾矿砀码砖砗砚砜砺砻砾础硁硅硕硖硗硙硚确硷碍碛碜碱碹磙礼祎祢祯祷祸禀禄禅离秃秆种积称秽秾稆税稣稳穑穷窃窍窑窜窝窥窦窭竖竞笃笋笔笕笺笼笾筑筚筛筜筝筹签简箓箦箧箨箩箪箫篑篓篮篱簖籁籴类籼粜粝粤粪粮糁糇紧絷纟纠纡红纣纤纥约级纨纩纪纫纬纭纮纯纰纱纲纳纴纵纶纷纸纹纺纻纼纽纾线绀绁绂练组绅细织终绉绊绋绌绍绎经绐绑绒结绔绕绖绗绘给绚绛络绝绞统绠绡绢绣绤绥绦继绨绩绪绫绬续绮绯绰绱绲绳维绵绶绷绸绹绺绻综绽绾绿缀缁缂缃缄缅缆缇缈缉缊缋缌缍缎缏缐缑缒缓缔缕编缗缘缙缚缛缜缝缞缟缠缡缢缣缤缥缦缧缨缩缪缫缬缭缮缯缰缱缲缳缴缵罂网罗罚罢罴羁羟羡翘翙翚耢耧耸耻聂聋职聍联聩聪肃肠肤肷肾肿胀胁胆胜胧胨胪胫胶脉脍脏脐脑脓脔脚脱脶脸腊腌腘腭腻腼腽腾膑臜舆舣舰舱舻艰艳艹艺节芈芗芜芦苁苇苈苋苌苍苎苏苘苹茎茏茑茔茕茧荆荐荙荚荛荜荞荟荠荡荣荤荥荦荧荨荩荪荫荬荭荮药莅莜莱莲莳莴莶获莸莹莺莼萚萝萤营萦萧萨葱蒇蒉蒋蒌蓝蓟蓠蓣蓥蓦蔷蔹蔺蔼蕲蕴薮藁藓虏虑虚虫虬虮虽虾虿蚀蚁蚂蚕蚝蚬蛊蛎蛏蛮蛰蛱蛲蛳蛴蜕蜗蜡蝇蝈蝉蝎蝼蝾螀螨蟏衅衔补衬衮袄袅袆袜袭袯装裆裈裢裣裤裥褛褴襁襕见观觃规觅视觇览觉觊觋觌觍觎觏觐觑觞触觯詟誉誊讠计订讣认讥讦讧讨让讪讫训议讯记讱讲讳讴讵讶讷许讹论讻讼讽设访诀证诂诃评诅识诇诈诉诊诋诌词诎诏诐译诒诓诔试诖诗诘诙诚诛诜话诞诟诠诡询诣诤该详诧诨诩诪诫诬语诮误诰诱诲诳说诵诶请诸诹诺读诼诽课诿谀谁谂调谄谅谆谇谈谊谋谌谍谎谏谐谑谒谓谔谕谖谗谘谙谚谛谜谝谞谟谠谡谢谣谤谥谦谧谨谩谪谫谬谭谮谯谰谱谲谳谴谵谶谷豮贝贞负贠贡财责贤败账货质贩贪贫贬购贮贯贰贱贲贳贴贵贶贷贸费贺贻贼贽贾贿赀赁赂赃资赅赆赇赈赉赊赋赌赍赎赏赐赑赒赓赔赕赖赗赘赙赚赛赜赝赞赟赠赡赢赣赪赵赶趋趱趸跃跄跖跞践跶跷跸跹跻踊踌踪踬踯蹑蹒蹰蹿躏躜躯车轧轨轩轪轫转轭轮软轰轱轲轳轴轵轶轷轸轹轺轻轼载轾轿辀辁辂较辄辅辆辇辈辉辊辋辌辍辎辏辐辑辒输辔辕辖辗辘辙辚辞辩辫边辽达迁过迈运还这进远违连迟迩迳迹适选逊递逦逻遗遥邓邝邬邮邹邺邻郁郄郏郐郑郓郦郧郸酝酦酱酽酾酿释里鉅鉴銮錾钆钇针钉钊钋钌钍钎钏钐钑钒钓钔钕钖钗钘钙钚钛钝钞钟钠钡钢钣钤钥钦钧钨钩钪钫钬钭钮钯钰钱钲钳钴钵钶钷钸钹钺钻钼钽钾钿铀铁铂铃铄铅铆铈铉铊铋铍铎铏铐铑铒铕铗铘铙铚铛铜铝铞铟铠铡铢铣铤铥铦铧铨铪铫铬铭铮铯铰铱铲铳铴铵银铷铸铹铺铻铼铽链铿销锁锂锃锄锅锆锇锈锉锊锋锌锍锎锏锐锑锒锓锔锕锖锗错锚锜锞锟锠锡锢锣锤锥锦锨锩锫锬锭键锯锰锱锲锳锴锵锶锷锸锹锺锻锼锽锾锿镀镁镂镃镆镇镈镉镊镌镍镎镏镐镑镒镕镖镗镙镚镛镜镝镞镟镠镡镢镣镤镥镦镧镨镩镪镫镬镭镮镯镰镱镲镳镴镶长门闩闪闫闬闭问闯闰闱闲闳间闵闶闷闸闹闺闻闼闽闾闿阀阁阂阃阄阅阆阇阈阉阊阋阌阍阎阏阐阑阒阓阔阕阖阗阘阙阚阛队阳阴阵阶际陆陇陈陉陕陧陨险随隐隶隽难雏雠雳雾霁霉霭靓静靥鞑鞒鞯鞴韦韧韨韩韪韫韬韵页顶顷顸项顺须顼顽顾顿颀颁颂颃预颅领颇颈颉颊颋颌颍颎颏颐频颒颓颔颕颖颗题颙颚颛颜额颞颟颠颡颢颣颤颥颦颧风飏飐飑飒飓飔飕飖飗飘飙飚飞飨餍饤饥饦饧饨饩饪饫饬饭饮饯饰饱饲饳饴饵饶饷饸饹饺饻饼饽饾饿馀馁馂馃馄馅馆馇馈馉馊馋馌馍馎馏馐馑馒馓馔馕马驭驮驯驰驱驲驳驴驵驶驷驸驹驺驻驼驽驾驿骀骁骂骃骄骅骆骇骈骉骊骋验骍骎骏骐骑骒骓骔骕骖骗骘骙骚骛骜骝骞骟骠骡骢骣骤骥骦骧髅髋髌鬓魇魉鱼鱽鱾鱿鲀鲁鲂鲄鲅鲆鲇鲈鲉鲊鲋鲌鲍鲎鲏鲐鲑鲒鲓鲔鲕鲖鲗鲘鲙鲚鲛鲜鲝鲞鲟鲠鲡鲢鲣鲤鲥鲦鲧鲨鲩鲪鲫鲬鲭鲮鲯鲰鲱鲲鲳鲴鲵鲶鲷鲸鲹鲺鲻鲼鲽鲾鲿鳀鳁鳂鳃鳄鳅鳆鳇鳈鳉鳊鳋鳌鳍鳎鳏鳐鳑鳒鳓鳔鳕鳖鳗鳘鳙鳛鳜鳝鳞鳟鳠鳡鳢鳣鸟鸠鸡鸢鸣鸤鸥鸦鸧鸨鸩鸪鸫鸬鸭鸮鸯鸰鸱鸲鸳鸴鸵鸶鸷鸸鸹鸺鸻鸼鸽鸾鸿鹀鹁鹂鹃鹄鹅鹆鹇鹈鹉鹊鹋鹌鹍鹎鹏鹐鹑鹒鹓鹔鹕鹖鹗鹘鹚鹛鹜鹝鹞鹟鹠鹡鹢鹣鹤鹥鹦鹧鹨鹩鹪鹫鹬鹭鹯鹰鹱鹲鹳鹴鹾麦麸黄黉黡黩黪黾龙历志制一台皋准复猛钟注范签'
  const FTPYStr = () => '萬與醜專業叢東絲丟兩嚴喪個爿豐臨為麗舉麼義烏樂喬習鄉書買亂爭於虧雲亙亞產畝親褻嚲億僅從侖倉儀們價眾優夥會傴傘偉傳傷倀倫傖偽佇體餘傭僉俠侶僥偵側僑儈儕儂俁儔儼倆儷儉債傾傯僂僨償儻儐儲儺兒兌兗黨蘭關興茲養獸囅內岡冊寫軍農塚馮衝決況凍淨淒涼淩減湊凜幾鳳鳧憑凱擊氹鑿芻劃劉則剛創刪別剗剄劊劌剴劑剮劍剝劇勸辦務勱動勵勁勞勢勳猛勩勻匭匱區醫華協單賣盧鹵臥衛卻巹廠廳曆厲壓厭厙廁廂厴廈廚廄廝縣參靉靆雙發變敘疊葉號歎嘰籲後嚇呂嗎唚噸聽啟吳嘸囈嘔嚦唄員咼嗆嗚詠哢嚨嚀噝吒噅鹹呱響啞噠嘵嗶噦嘩噲嚌噥喲嘜嗊嘮啢嗩唕喚呼嘖嗇囀齧囉嘽嘯噴嘍嚳囁嗬噯噓嚶囑嚕劈囂謔團園囪圍圇國圖圓聖壙場阪壞塊堅壇壢壩塢墳墜壟壟壚壘墾坰堊墊埡墶壋塏堖塒塤堝墊垵塹墮壪牆壯聲殼壺壼處備複夠頭誇夾奪奩奐奮獎奧妝婦媽嫵嫗媯姍薑婁婭嬈嬌孌娛媧嫻嫿嬰嬋嬸媼嬡嬪嬙嬤孫學孿寧寶實寵審憲宮寬賓寢對尋導壽將爾塵堯尷屍盡層屭屜屆屬屢屨嶼歲豈嶇崗峴嶴嵐島嶺嶽崠巋嶨嶧峽嶢嶠崢巒嶗崍嶮嶄嶸嶔崳嶁脊巔鞏巰幣帥師幃帳簾幟帶幀幫幬幘幗冪襆幹並廣莊慶廬廡庫應廟龐廢廎廩開異棄張彌弳彎彈強歸當錄彠彥徹徑徠禦憶懺憂愾懷態慫憮慪悵愴憐總懟懌戀懇惡慟懨愷惻惱惲悅愨懸慳憫驚懼慘懲憊愜慚憚慣湣慍憤憒願懾憖怵懣懶懍戇戔戲戧戰戩戶紮撲扡執擴捫掃揚擾撫拋摶摳掄搶護報擔擬攏揀擁攔擰撥擇掛摯攣掗撾撻挾撓擋撟掙擠揮撏撈損撿換搗據撚擄摑擲撣摻摜摣攬撳攙擱摟攪攜攝攄擺搖擯攤攖撐攆擷擼攛擻攢敵斂數齋斕鬥斬斷無舊時曠暘曇晝曨顯晉曬曉曄暈暉暫曖劄術樸機殺雜權條來楊榪傑極構樅樞棗櫪梘棖槍楓梟櫃檸檉梔柵標棧櫛櫳棟櫨櫟欄樹棲樣欒棬椏橈楨檔榿橋樺檜槳樁夢檮棶檢欞槨櫝槧欏橢樓欖櫬櫚櫸檟檻檳櫧橫檣櫻櫫櫥櫓櫞簷檁歡歟歐殲歿殤殘殞殮殫殯毆毀轂畢斃氈毿氌氣氫氬氳彙漢汙湯洶遝溝沒灃漚瀝淪滄渢溈滬濔濘淚澩瀧瀘濼瀉潑澤涇潔灑窪浹淺漿澆湞溮濁測澮濟瀏滻渾滸濃潯濜塗湧濤澇淶漣潿渦溳渙滌潤澗漲澀澱淵淥漬瀆漸澠漁瀋滲溫遊灣濕潰濺漵漊潷滾滯灩灄滿瀅濾濫灤濱灘澦濫瀠瀟瀲濰潛瀦瀾瀨瀕灝滅燈靈災燦煬爐燉煒熗點煉熾爍爛烴燭煙煩燒燁燴燙燼熱煥燜燾煆糊溜愛爺牘犛牽犧犢強狀獷獁猶狽麅獮獰獨狹獅獪猙獄猻獫獵獼玀豬貓蝟獻獺璣璵瑒瑪瑋環現瑲璽瑉玨琺瓏璫琿璡璉瑣瓊瑤璦璿瓔瓚甕甌電畫暢佘疇癤療瘧癘瘍鬁瘡瘋皰屙癰痙癢瘂癆瘓癇癡癉瘮瘞瘺癟癱癮癭癩癬癲臒皚皺皸盞鹽監蓋盜盤瞘眥矓著睜睞瞼瞞矚矯磯礬礦碭碼磚硨硯碸礪礱礫礎硜矽碩硤磽磑礄確鹼礙磧磣堿镟滾禮禕禰禎禱禍稟祿禪離禿稈種積稱穢穠穭稅穌穩穡窮竊竅窯竄窩窺竇窶豎競篤筍筆筧箋籠籩築篳篩簹箏籌簽簡籙簀篋籜籮簞簫簣簍籃籬籪籟糴類秈糶糲粵糞糧糝餱緊縶糸糾紆紅紂纖紇約級紈纊紀紉緯紜紘純紕紗綱納紝縱綸紛紙紋紡紵紖紐紓線紺絏紱練組紳細織終縐絆紼絀紹繹經紿綁絨結絝繞絰絎繪給絢絳絡絕絞統綆綃絹繡綌綏絛繼綈績緒綾緓續綺緋綽緔緄繩維綿綬繃綢綯綹綣綜綻綰綠綴緇緙緗緘緬纜緹緲緝縕繢緦綞緞緶線緱縋緩締縷編緡緣縉縛縟縝縫縗縞纏縭縊縑繽縹縵縲纓縮繆繅纈繚繕繒韁繾繰繯繳纘罌網羅罰罷羆羈羥羨翹翽翬耮耬聳恥聶聾職聹聯聵聰肅腸膚膁腎腫脹脅膽勝朧腖臚脛膠脈膾髒臍腦膿臠腳脫腡臉臘醃膕齶膩靦膃騰臏臢輿艤艦艙艫艱豔艸藝節羋薌蕪蘆蓯葦藶莧萇蒼苧蘇檾蘋莖蘢蔦塋煢繭荊薦薘莢蕘蓽蕎薈薺蕩榮葷滎犖熒蕁藎蓀蔭蕒葒葤藥蒞蓧萊蓮蒔萵薟獲蕕瑩鶯蓴蘀蘿螢營縈蕭薩蔥蕆蕢蔣蔞藍薊蘺蕷鎣驀薔蘞藺藹蘄蘊藪槁蘚虜慮虛蟲虯蟣雖蝦蠆蝕蟻螞蠶蠔蜆蠱蠣蟶蠻蟄蛺蟯螄蠐蛻蝸蠟蠅蟈蟬蠍螻蠑螿蟎蠨釁銜補襯袞襖嫋褘襪襲襏裝襠褌褳襝褲襇褸襤繈襴見觀覎規覓視覘覽覺覬覡覿覥覦覯覲覷觴觸觶讋譽謄訁計訂訃認譏訐訌討讓訕訖訓議訊記訒講諱謳詎訝訥許訛論訩訟諷設訪訣證詁訶評詛識詗詐訴診詆謅詞詘詔詖譯詒誆誄試詿詩詰詼誠誅詵話誕詬詮詭詢詣諍該詳詫諢詡譸誡誣語誚誤誥誘誨誑說誦誒請諸諏諾讀諑誹課諉諛誰諗調諂諒諄誶談誼謀諶諜謊諫諧謔謁謂諤諭諼讒諮諳諺諦謎諞諝謨讜謖謝謠謗諡謙謐謹謾謫譾謬譚譖譙讕譜譎讞譴譫讖穀豶貝貞負貟貢財責賢敗賬貨質販貪貧貶購貯貫貳賤賁貰貼貴貺貸貿費賀貽賊贄賈賄貲賃賂贓資賅贐賕賑賚賒賦賭齎贖賞賜贔賙賡賠賧賴賵贅賻賺賽賾贗讚贇贈贍贏贛赬趙趕趨趲躉躍蹌蹠躒踐躂蹺蹕躚躋踴躊蹤躓躑躡蹣躕躥躪躦軀車軋軌軒軑軔轉軛輪軟轟軲軻轤軸軹軼軤軫轢軺輕軾載輊轎輈輇輅較輒輔輛輦輩輝輥輞輬輟輜輳輻輯轀輸轡轅轄輾轆轍轔辭辯辮邊遼達遷過邁運還這進遠違連遲邇逕跡適選遜遞邐邏遺遙鄧鄺鄔郵鄒鄴鄰鬱郤郟鄶鄭鄆酈鄖鄲醞醱醬釅釃釀釋裏钜鑒鑾鏨釓釔針釘釗釙釕釷釺釧釤鈒釩釣鍆釹鍚釵鈃鈣鈈鈦鈍鈔鍾鈉鋇鋼鈑鈐鑰欽鈞鎢鉤鈧鈁鈥鈄鈕鈀鈺錢鉦鉗鈷缽鈳鉕鈽鈸鉞鑽鉬鉭鉀鈿鈾鐵鉑鈴鑠鉛鉚鈰鉉鉈鉍鈹鐸鉶銬銠鉺銪鋏鋣鐃銍鐺銅鋁銱銦鎧鍘銖銑鋌銩銛鏵銓鉿銚鉻銘錚銫鉸銥鏟銃鐋銨銀銣鑄鐒鋪鋙錸鋱鏈鏗銷鎖鋰鋥鋤鍋鋯鋨鏽銼鋝鋒鋅鋶鐦鐧銳銻鋃鋟鋦錒錆鍺錯錨錡錁錕錩錫錮鑼錘錐錦鍁錈錇錟錠鍵鋸錳錙鍥鍈鍇鏘鍶鍔鍤鍬鍾鍛鎪鍠鍰鎄鍍鎂鏤鎡鏌鎮鎛鎘鑷鐫鎳鎿鎦鎬鎊鎰鎔鏢鏜鏍鏰鏞鏡鏑鏃鏇鏐鐔钁鐐鏷鑥鐓鑭鐠鑹鏹鐙鑊鐳鐶鐲鐮鐿鑔鑣鑞鑲長門閂閃閆閈閉問闖閏闈閑閎間閔閌悶閘鬧閨聞闥閩閭闓閥閣閡閫鬮閱閬闍閾閹閶鬩閿閽閻閼闡闌闃闠闊闋闔闐闒闕闞闤隊陽陰陣階際陸隴陳陘陝隉隕險隨隱隸雋難雛讎靂霧霽黴靄靚靜靨韃鞽韉韝韋韌韍韓韙韞韜韻頁頂頃頇項順須頊頑顧頓頎頒頌頏預顱領頗頸頡頰頲頜潁熲頦頤頻頮頹頷頴穎顆題顒顎顓顏額顳顢顛顙顥纇顫顬顰顴風颺颭颮颯颶颸颼颻飀飄飆飆飛饗饜飣饑飥餳飩餼飪飫飭飯飲餞飾飽飼飿飴餌饒餉餄餎餃餏餅餑餖餓餘餒餕餜餛餡館餷饋餶餿饞饁饃餺餾饈饉饅饊饌饢馬馭馱馴馳驅馹駁驢駔駛駟駙駒騶駐駝駑駕驛駘驍罵駰驕驊駱駭駢驫驪騁驗騂駸駿騏騎騍騅騌驌驂騙騭騤騷騖驁騮騫騸驃騾驄驏驟驥驦驤髏髖髕鬢魘魎魚魛魢魷魨魯魴魺鮁鮃鯰鱸鮋鮓鮒鮊鮑鱟鮍鮐鮭鮚鮳鮪鮞鮦鰂鮜鱠鱭鮫鮮鮺鯗鱘鯁鱺鰱鰹鯉鰣鰷鯀鯊鯇鮶鯽鯒鯖鯪鯕鯫鯡鯤鯧鯝鯢鯰鯛鯨鯵鯴鯔鱝鰈鰏鱨鯷鰮鰃鰓鱷鰍鰒鰉鰁鱂鯿鰠鼇鰭鰨鰥鰩鰟鰜鰳鰾鱈鱉鰻鰵鱅鰼鱖鱔鱗鱒鱯鱤鱧鱣鳥鳩雞鳶鳴鳲鷗鴉鶬鴇鴆鴣鶇鸕鴨鴞鴦鴒鴟鴝鴛鴬鴕鷥鷙鴯鴰鵂鴴鵃鴿鸞鴻鵐鵓鸝鵑鵠鵝鵒鷳鵜鵡鵲鶓鵪鶤鵯鵬鵮鶉鶊鵷鷫鶘鶡鶚鶻鶿鶥鶩鷊鷂鶲鶹鶺鷁鶼鶴鷖鸚鷓鷚鷯鷦鷲鷸鷺鸇鷹鸌鸏鸛鸘鹺麥麩黃黌黶黷黲黽龍歷誌製壹臺臯準復勐鐘註範籤'

  const Traditionalized = (cc) => {
    let str = ''
    const ss = JTPYStr()
    const tt = FTPYStr()
    for (let i = 0; i < cc.length; i++) {
      if (cc.charCodeAt(i) > 10000 && ss.indexOf(cc.charAt(i)) !== -1) {
        str += tt.charAt(ss.indexOf(cc.charAt(i)))
      } else str += cc.charAt(i)
    }
    return str
  }

  const Simplized = (cc) => {
    let str = ''
    const ss = JTPYStr()
    const tt = FTPYStr()
    for (let i = 0; i < cc.length; i++) {
      if (cc.charCodeAt(i) > 10000 && tt.indexOf(cc.charAt(i)) !== -1) {
        str += ss.charAt(tt.indexOf(cc.charAt(i)))
      } else str += cc.charAt(i)
    }
    return str
  }

  const translateInitialization = () => {
    if (translateButtonObject) {
      if (currentEncoding !== targetEncoding) {
        translateButtonObject.textContent =
          targetEncoding === 1
            ? msgToSimplifiedChinese
            : msgToTraditionalChinese
        setLang()
        setTimeout(translateBody, translateDelay)
      }
    }
  }

  window.translateFn = {
    translatePage,
    Traditionalized,
    Simplized,
    translateInitialization
  }

  translateInitialization()
  btf.addGlobalFn('pjaxComplete', translateInitialization, 'translateInitialization')
})

```

### 文件路径: `themes\butterfly\source\js\utils.js`
```js
(() => {
  const btfFn = {
    debounce: (func, wait = 0, immediate = false) => {
      let timeout
      return (...args) => {
        const later = () => {
          timeout = null
          if (!immediate) func(...args)
        }
        const callNow = immediate && !timeout
        clearTimeout(timeout)
        timeout = setTimeout(later, wait)
        if (callNow) func(...args)
      }
    },

    throttle: function (func, wait, options = {}) {
      let timeout, context, args
      let previous = 0

      const later = () => {
        previous = options.leading === false ? 0 : new Date().getTime()
        timeout = null
        func.apply(context, args)
        if (!timeout) context = args = null
      }

      const throttled = (...params) => {
        const now = new Date().getTime()
        if (!previous && options.leading === false) previous = now
        const remaining = wait - (now - previous)
        context = this
        args = params
        if (remaining <= 0 || remaining > wait) {
          if (timeout) {
            clearTimeout(timeout)
            timeout = null
          }
          previous = now
          func.apply(context, args)
          if (!timeout) context = args = null
        } else if (!timeout && options.trailing !== false) {
          timeout = setTimeout(later, remaining)
        }
      }

      return throttled
    },

    overflowPaddingR: {
      add: () => {
        const paddingRight = window.innerWidth - document.body.clientWidth

        if (paddingRight > 0) {
          document.body.style.paddingRight = `${paddingRight}px`
          document.body.style.overflow = 'hidden'
          const menuElement = document.querySelector('#page-header.nav-fixed #menus')
          if (menuElement) {
            menuElement.style.paddingRight = `${paddingRight}px`
          }
        }
      },
      remove: () => {
        document.body.style.paddingRight = ''
        document.body.style.overflow = ''
        const menuElement = document.querySelector('#page-header.nav-fixed #menus')
        if (menuElement) {
          menuElement.style.paddingRight = ''
        }
      }
    },

    snackbarShow: (text, showAction = false, duration = 2000) => {
      const { position, bgLight, bgDark } = GLOBAL_CONFIG.Snackbar
      const bg = document.documentElement.getAttribute('data-theme') === 'light' ? bgLight : bgDark
      Snackbar.show({
        text,
        backgroundColor: bg,
        showAction,
        duration,
        pos: position,
        customClass: 'snackbar-css'
      })
    },

    diffDate: (inputDate, more = false) => {
      const dateNow = new Date()
      const datePost = new Date(inputDate)
      const diffMs = dateNow - datePost
      const diffSec = diffMs / 1000
      const diffMin = diffSec / 60
      const diffHour = diffMin / 60
      const diffDay = diffHour / 24
      const diffMonth = diffDay / 30
      const { dateSuffix } = GLOBAL_CONFIG

      if (!more) return Math.floor(diffDay)

      if (diffMonth > 12) return datePost.toISOString().slice(0, 10)
      if (diffMonth >= 1) return `${Math.floor(diffMonth)} ${dateSuffix.month}`
      if (diffDay >= 1) return `${Math.floor(diffDay)} ${dateSuffix.day}`
      if (diffHour >= 1) return `${Math.floor(diffHour)} ${dateSuffix.hour}`
      if (diffMin >= 1) return `${Math.floor(diffMin)} ${dateSuffix.min}`
      return dateSuffix.just
    },

    loadComment: (dom, callback) => {
      if ('IntersectionObserver' in window) {
        const observerItem = new IntersectionObserver((entries) => {
          if (entries[0].isIntersecting) {
            callback()
            observerItem.disconnect()
          }
        }, { threshold: [0] })
        observerItem.observe(dom)
      } else {
        callback()
      }
    },

    scrollToDest: (pos, time = 500) => {
      const currentPos = window.scrollY
      const isNavFixed = document.getElementById('page-header').classList.contains('fixed')
      if (currentPos > pos || isNavFixed) pos = pos - 70

      if ('scrollBehavior' in document.documentElement.style) {
        window.scrollTo({
          top: pos,
          behavior: 'smooth'
        })
        return
      }

      const startTime = performance.now()
      const animate = currentTime => {
        const timeElapsed = currentTime - startTime
        const progress = Math.min(timeElapsed / time, 1)
        window.scrollTo(0, currentPos + (pos - currentPos) * progress)
        if (progress < 1) {
          requestAnimationFrame(animate)
        }
      }
      requestAnimationFrame(animate)
    },

    animateIn: (ele, animation) => {
      ele.style.display = 'block'
      ele.style.animation = animation
    },

    animateOut: (ele, animation) => {
      const handleAnimationEnd = () => {
        ele.style.display = ''
        ele.style.animation = ''
        ele.removeEventListener('animationend', handleAnimationEnd)
      }
      ele.addEventListener('animationend', handleAnimationEnd)
      ele.style.animation = animation
    },

    wrap: (selector, eleType, options) => {
      const createEle = document.createElement(eleType)
      for (const [key, value] of Object.entries(options)) {
        createEle.setAttribute(key, value)
      }
      selector.parentNode.insertBefore(createEle, selector)
      createEle.appendChild(selector)
    },

    isHidden: ele => ele.offsetHeight === 0 && ele.offsetWidth === 0,

    getEleTop: ele => {
      let actualTop = ele.offsetTop
      let current = ele.offsetParent

      while (current !== null) {
        actualTop += current.offsetTop
        current = current.offsetParent
      }

      return actualTop
    },

    loadLightbox: ele => {
      const service = GLOBAL_CONFIG.lightbox

      if (service === 'medium_zoom') {
        mediumZoom(ele, { background: 'var(--zoom-bg)' })
      }

      if (service === 'fancybox') {
        Array.from(ele).forEach(i => {
          if (i.parentNode.tagName !== 'A') {
            const dataSrc = i.dataset.lazySrc || i.src
            const dataCaption = i.title || i.alt || ''
            btf.wrap(i, 'a', { href: dataSrc, 'data-fancybox': 'gallery', 'data-caption': dataCaption, 'data-thumb': dataSrc })
          }
        })

        if (!window.fancyboxRun) {
          Fancybox.bind('[data-fancybox]', {
            Hash: false,
            Thumbs: {
              showOnStart: false
            },
            Images: {
              Panzoom: {
                maxScale: 4
              }
            },
            Carousel: {
              transition: 'slide'
            },
            Toolbar: {
              display: {
                left: ['infobar'],
                middle: [
                  'zoomIn',
                  'zoomOut',
                  'toggle1to1',
                  'rotateCCW',
                  'rotateCW',
                  'flipX',
                  'flipY'
                ],
                right: ['slideshow', 'thumbs', 'close']
              }
            }
          })
          window.fancyboxRun = true
        }
      }
    },

    setLoading: {
      add: ele => {
        const html = `
        <div class="loading-container">
          <div class="loading-item">
            <div></div><div></div><div></div><div></div><div></div>
          </div>
        </div>
      `
        ele.insertAdjacentHTML('afterend', html)
      },
      remove: ele => {
        ele.nextElementSibling.remove()
      }
    },

    updateAnchor: anchor => {
      if (anchor !== window.location.hash) {
        if (!anchor) anchor = location.pathname
        const title = GLOBAL_CONFIG_SITE.title
        window.history.replaceState({
          url: location.href,
          title
        }, title, anchor)
      }
    },

    getScrollPercent: (() => {
      let docHeight, winHeight, headerHeight, contentMath

      return (currentTop, ele) => {
        if (!docHeight || ele.clientHeight !== docHeight) {
          docHeight = ele.clientHeight
          winHeight = window.innerHeight
          headerHeight = ele.offsetTop
          contentMath = Math.max(docHeight - winHeight, document.documentElement.scrollHeight - winHeight)
        }

        const scrollPercent = (currentTop - headerHeight) / contentMath
        return Math.max(0, Math.min(100, Math.round(scrollPercent * 100)))
      }
    })(),

    addEventListenerPjax: (ele, event, fn, option = false) => {
      ele.addEventListener(event, fn, option)
      btf.addGlobalFn('pjaxSendOnce', () => {
        ele.removeEventListener(event, fn, option)
      })
    },

    removeGlobalFnEvent: (key, parent = window) => {
      const globalFn = parent.globalFn || {}
      const keyObj = globalFn[key]
      if (!keyObj) return

      Object.keys(keyObj).forEach(i => keyObj[i]())

      delete globalFn[key]
    },

    switchComments: (el = document, path) => {
      const switchBtn = el.querySelector('#switch-btn')
      if (!switchBtn) return

      let switchDone = false
      const postComment = el.querySelector('#post-comment')
      const handleSwitchBtn = () => {
        postComment.classList.toggle('move')
        if (!switchDone && typeof loadOtherComment === 'function') {
          switchDone = true
          loadOtherComment(el, path)
        }
      }
      btf.addEventListenerPjax(switchBtn, 'click', handleSwitchBtn)
    }
  }

  window.btf = { ...window.btf, ...btfFn }
})()

```

### 文件路径: `themes\butterfly\source\js\search\algolia.js`
```js
window.addEventListener('load', () => {
  const { algolia } = GLOBAL_CONFIG
  const { appId, apiKey, indexName, hitsPerPage = 5, languages } = algolia

  if (!appId || !apiKey || !indexName) {
    return console.error('Algolia setting is invalid!')
  }

  const $searchMask = document.getElementById('search-mask')
  const $searchDialog = document.querySelector('#algolia-search .search-dialog')

  const animateElements = show => {
    const action = show ? 'animateIn' : 'animateOut'
    const maskAnimation = show ? 'to_show 0.5s' : 'to_hide 0.5s'
    const dialogAnimation = show ? 'titleScale 0.5s' : 'search_close .5s'
    btf[action]($searchMask, maskAnimation)
    btf[action]($searchDialog, dialogAnimation)
  }

  const fixSafariHeight = () => {
    if (window.innerWidth < 768) {
      $searchDialog.style.setProperty('--search-height', `${window.innerHeight}px`)
    }
  }

  const openSearch = () => {
    btf.overflowPaddingR.add()
    animateElements(true)
    setTimeout(() => { document.querySelector('#algolia-search .ais-SearchBox-input').focus() }, 100)

    const handleEscape = event => {
      if (event.code === 'Escape') {
        closeSearch()
        document.removeEventListener('keydown', handleEscape)
      }
    }

    document.addEventListener('keydown', handleEscape)
    fixSafariHeight()
    window.addEventListener('resize', fixSafariHeight)
  }

  const closeSearch = () => {
    btf.overflowPaddingR.remove()
    animateElements(false)
    window.removeEventListener('resize', fixSafariHeight)
  }

  const searchClickFn = () => {
    btf.addEventListenerPjax(document.querySelector('#search-button > .search'), 'click', openSearch)
  }

  const searchFnOnce = () => {
    $searchMask.addEventListener('click', closeSearch)
    document.querySelector('#algolia-search .search-close-button').addEventListener('click', closeSearch)
  }

  const cutContent = (content) => {
    if (!content) return ''
    const firstOccur = content.indexOf('<mark>')
    let start = firstOccur - 30
    let end = firstOccur + 120
    let pre = ''
    let post = ''

    if (start <= 0) {
      start = 0
      end = 140
    } else {
      pre = '...'
    }

    if (end > content.length) {
      end = content.length
    } else {
      post = '...'
    }

    return `${pre}${content.substring(start, end)}${post}`
  }

  const disableDiv = [
    document.getElementById('algolia-hits'),
    document.getElementById('algolia-pagination'),
    document.querySelector('#algolia-info .algolia-stats')
  ]

  const searchClient = typeof algoliasearch === 'function' ? algoliasearch : window['algoliasearch/lite'].liteClient
  const search = instantsearch({
    indexName,
    searchClient: searchClient(appId, apiKey),
    searchFunction (helper) {
      disableDiv.forEach(item => {
        item.style.display = helper.state.query ? '' : 'none'
      })
      if (helper.state.query) helper.search()
    }
  })

  const widgets = [
    instantsearch.widgets.configure({ hitsPerPage }),
    instantsearch.widgets.searchBox({
      container: '#algolia-search-input',
      showReset: false,
      showSubmit: false,
      placeholder: languages.input_placeholder,
      showLoadingIndicator: true
    }),
    instantsearch.widgets.hits({
      container: '#algolia-hits',
      templates: {
        item (data) {
          const link = data.permalink || (GLOBAL_CONFIG.root + data.path)
          const result = data._highlightResult
          const content = result.contentStripTruncate
            ? cutContent(result.contentStripTruncate.value)
            : result.contentStrip
              ? cutContent(result.contentStrip.value)
              : result.content
                ? cutContent(result.content.value)
                : ''
          return `
            <a href="${link}" class="algolia-hit-item-link">
              <span class="algolia-hits-item-title">${result.title.value || 'no-title'}</span>
              ${content ? `<div class="algolia-hit-item-content">${content}</div>` : ''}
            </a>`
        },
        empty (data) {
          return `<div id="algolia-hits-empty">${languages.hits_empty.replace(/\$\{query}/, data.query)}</div>`
        }
      }
    }),
    instantsearch.widgets.stats({
      container: '#algolia-info > .algolia-stats',
      templates: {
        text (data) {
          const stats = languages.hits_stats
            .replace(/\$\{hits}/, data.nbHits)
            .replace(/\$\{time}/, data.processingTimeMS)
          return `<hr>${stats}`
        }
      }
    }),
    instantsearch.widgets.poweredBy({
      container: '#algolia-info > .algolia-poweredBy'
    }),
    instantsearch.widgets.pagination({
      container: '#algolia-pagination',
      totalPages: 5,
      templates: {
        first: '<i class="fas fa-angle-double-left"></i>',
        last: '<i class="fas fa-angle-double-right"></i>',
        previous: '<i class="fas fa-angle-left"></i>',
        next: '<i class="fas fa-angle-right"></i>'
      }
    })
  ]

  search.addWidgets(widgets)
  search.start()
  searchClickFn()
  searchFnOnce()

  window.addEventListener('pjax:complete', () => {
    if (!btf.isHidden($searchMask)) closeSearch()
    searchClickFn()
  })

  if (window.pjax) {
    search.on('render', () => {
      window.pjax.refresh(document.getElementById('algolia-hits'))
    })
  }
})

```

### 文件路径: `themes\butterfly\source\js\search\local-search.js`
```js
/**
 * Refer to hexo-generator-searchdb
 * https://github.com/next-theme/hexo-generator-searchdb/blob/main/dist/search.js
 * Modified by hexo-theme-butterfly
 */

class LocalSearch {
  constructor ({
    path = '',
    unescape = false,
    top_n_per_article = 1
  }) {
    this.path = path
    this.unescape = unescape
    this.top_n_per_article = top_n_per_article
    this.isfetched = false
    this.datas = null
  }

  getIndexByWord (words, text, caseSensitive = false) {
    const index = []
    const included = new Set()

    if (!caseSensitive) {
      text = text.toLowerCase()
    }
    words.forEach(word => {
      if (this.unescape) {
        const div = document.createElement('div')
        div.innerText = word
        word = div.innerHTML
      }
      const wordLen = word.length
      if (wordLen === 0) return
      let startPosition = 0
      let position = -1
      if (!caseSensitive) {
        word = word.toLowerCase()
      }
      while ((position = text.indexOf(word, startPosition)) > -1) {
        index.push({ position, word })
        included.add(word)
        startPosition = position + wordLen
      }
    })
    // Sort index by position of keyword
    index.sort((left, right) => {
      if (left.position !== right.position) {
        return left.position - right.position
      }
      return right.word.length - left.word.length
    })
    return [index, included]
  }

  // Merge hits into slices
  mergeIntoSlice (start, end, index) {
    let item = index[0]
    let { position, word } = item
    const hits = []
    const count = new Set()
    while (position + word.length <= end && index.length !== 0) {
      count.add(word)
      hits.push({
        position,
        length: word.length
      })
      const wordEnd = position + word.length

      // Move to next position of hit
      index.shift()
      while (index.length !== 0) {
        item = index[0]
        position = item.position
        word = item.word
        if (wordEnd > position) {
          index.shift()
        } else {
          break
        }
      }
    }
    return {
      hits,
      start,
      end,
      count: count.size
    }
  }

  // Highlight title and content
  highlightKeyword (val, slice) {
    let result = ''
    let index = slice.start
    for (const { position, length } of slice.hits) {
      result += val.substring(index, position)
      index = position + length
      result += `<mark class="search-keyword">${val.substr(position, length)}</mark>`
    }
    result += val.substring(index, slice.end)
    return result
  }

  getResultItems (keywords) {
    const resultItems = []
    this.datas.forEach(({ title, content, url }) => {
      // The number of different keywords included in the article.
      const [indexOfTitle, keysOfTitle] = this.getIndexByWord(keywords, title)
      const [indexOfContent, keysOfContent] = this.getIndexByWord(keywords, content)
      const includedCount = new Set([...keysOfTitle, ...keysOfContent]).size

      // Show search results
      const hitCount = indexOfTitle.length + indexOfContent.length
      if (hitCount === 0) return

      const slicesOfTitle = []
      if (indexOfTitle.length !== 0) {
        slicesOfTitle.push(this.mergeIntoSlice(0, title.length, indexOfTitle))
      }

      let slicesOfContent = []
      while (indexOfContent.length !== 0) {
        const item = indexOfContent[0]
        const { position } = item
        // Cut out 120 characters. The maxlength of .search-input is 80.
        const start = Math.max(0, position - 20)
        const end = Math.min(content.length, position + 100)
        slicesOfContent.push(this.mergeIntoSlice(start, end, indexOfContent))
      }

      // Sort slices in content by included keywords' count and hits' count
      slicesOfContent.sort((left, right) => {
        if (left.count !== right.count) {
          return right.count - left.count
        } else if (left.hits.length !== right.hits.length) {
          return right.hits.length - left.hits.length
        }
        return left.start - right.start
      })

      // Select top N slices in content
      const upperBound = parseInt(this.top_n_per_article, 10)
      if (upperBound >= 0) {
        slicesOfContent = slicesOfContent.slice(0, upperBound)
      }

      let resultItem = ''

      url = new URL(url, location.origin)
      url.searchParams.append('highlight', keywords.join(' '))

      if (slicesOfTitle.length !== 0) {
        resultItem += `<li class="local-search-hit-item"><a href="${url.href}"><span class="search-result-title">${this.highlightKeyword(title, slicesOfTitle[0])}</span>`
      } else {
        resultItem += `<li class="local-search-hit-item"><a href="${url.href}"><span class="search-result-title">${title}</span>`
      }

      slicesOfContent.forEach(slice => {
        resultItem += `<p class="search-result">${this.highlightKeyword(content, slice)}...</p></a>`
      })

      resultItem += '</li>'
      resultItems.push({
        item: resultItem,
        id: resultItems.length,
        hitCount,
        includedCount
      })
    })
    return resultItems
  }

  fetchData () {
    const isXml = !this.path.endsWith('json')
    fetch(this.path)
      .then(response => response.text())
      .then(res => {
        // Get the contents from search data
        this.isfetched = true
        this.datas = isXml
          ? [...new DOMParser().parseFromString(res, 'text/xml').querySelectorAll('entry')].map(element => ({
              title: element.querySelector('title').textContent,
              content: element.querySelector('content').textContent,
              url: element.querySelector('url').textContent
            }))
          : JSON.parse(res)
        // Only match articles with non-empty titles
        this.datas = this.datas.filter(data => data.title).map(data => {
          data.title = data.title.trim()
          data.content = data.content ? data.content.trim().replace(/<[^>]+>/g, '') : ''
          data.url = decodeURIComponent(data.url).replace(/\/{2,}/g, '/')
          return data
        })
        // Remove loading animation
        window.dispatchEvent(new Event('search:loaded'))
      })
  }

  // Highlight by wrapping node in mark elements with the given class name
  highlightText (node, slice, className) {
    const val = node.nodeValue
    let index = slice.start
    const children = []
    for (const { position, length } of slice.hits) {
      const text = document.createTextNode(val.substring(index, position))
      index = position + length
      const mark = document.createElement('mark')
      mark.className = className
      mark.appendChild(document.createTextNode(val.substr(position, length)))
      children.push(text, mark)
    }
    node.nodeValue = val.substring(index, slice.end)
    children.forEach(element => {
      node.parentNode.insertBefore(element, node)
    })
  }

  // Highlight the search words provided in the url in the text
  highlightSearchWords (body) {
    const params = new URL(location.href).searchParams.get('highlight')
    const keywords = params ? params.split(' ') : []
    if (!keywords.length || !body) return
    const walk = document.createTreeWalker(body, NodeFilter.SHOW_TEXT, null)
    const allNodes = []
    while (walk.nextNode()) {
      if (!walk.currentNode.parentNode.matches('button, select, textarea, .mermaid')) allNodes.push(walk.currentNode)
    }
    allNodes.forEach(node => {
      const [indexOfNode] = this.getIndexByWord(keywords, node.nodeValue)
      if (!indexOfNode.length) return
      const slice = this.mergeIntoSlice(0, node.nodeValue.length, indexOfNode)
      this.highlightText(node, slice, 'search-keyword')
    })
  }
}

window.addEventListener('load', () => {
// Search
  const { path, top_n_per_article, unescape, languages } = GLOBAL_CONFIG.localSearch
  const localSearch = new LocalSearch({
    path,
    top_n_per_article,
    unescape
  })

  const input = document.querySelector('#local-search-input input')
  const statsItem = document.getElementById('local-search-stats-wrap')
  const $loadingStatus = document.getElementById('loading-status')
  const isXml = !path.endsWith('json')

  const inputEventFunction = () => {
    if (!localSearch.isfetched) return
    let searchText = input.value.trim().toLowerCase()
    isXml && (searchText = searchText.replace(/</g, '&lt;').replace(/>/g, '&gt;'))
    if (searchText !== '') $loadingStatus.innerHTML = '<i class="fas fa-spinner fa-pulse"></i>'
    const keywords = searchText.split(/[-\s]+/)
    const container = document.getElementById('local-search-results')
    let resultItems = []
    if (searchText.length > 0) {
    // Perform local searching
      resultItems = localSearch.getResultItems(keywords)
    }
    if (keywords.length === 1 && keywords[0] === '') {
      container.textContent = ''
      statsItem.textContent = ''
    } else if (resultItems.length === 0) {
      container.textContent = ''
      const statsDiv = document.createElement('div')
      statsDiv.className = 'search-result-stats'
      statsDiv.textContent = languages.hits_empty.replace(/\$\{query}/, searchText)
      statsItem.innerHTML = statsDiv.outerHTML
    } else {
      resultItems.sort((left, right) => {
        if (left.includedCount !== right.includedCount) {
          return right.includedCount - left.includedCount
        } else if (left.hitCount !== right.hitCount) {
          return right.hitCount - left.hitCount
        }
        return right.id - left.id
      })

      const stats = languages.hits_stats.replace(/\$\{hits}/, resultItems.length)

      container.innerHTML = `<ol class="search-result-list">${resultItems.map(result => result.item).join('')}</ol>`
      statsItem.innerHTML = `<hr><div class="search-result-stats">${stats}</div>`
      window.pjax && window.pjax.refresh(container)
    }

    $loadingStatus.textContent = ''
  }

  let loadFlag = false
  const $searchMask = document.getElementById('search-mask')
  const $searchDialog = document.querySelector('#local-search .search-dialog')

  // fix safari
  const fixSafariHeight = () => {
    if (window.innerWidth < 768) {
      $searchDialog.style.setProperty('--search-height', window.innerHeight + 'px')
    }
  }

  const openSearch = () => {
    btf.overflowPaddingR.add()
    btf.animateIn($searchMask, 'to_show 0.5s')
    btf.animateIn($searchDialog, 'titleScale 0.5s')
    setTimeout(() => { input.focus() }, 300)
    if (!loadFlag) {
      !localSearch.isfetched && localSearch.fetchData()
      input.addEventListener('input', inputEventFunction)
      loadFlag = true
    }
    // shortcut: ESC
    document.addEventListener('keydown', function f (event) {
      if (event.code === 'Escape') {
        closeSearch()
        document.removeEventListener('keydown', f)
      }
    })

    fixSafariHeight()
    window.addEventListener('resize', fixSafariHeight)
  }

  const closeSearch = () => {
    btf.overflowPaddingR.remove()
    btf.animateOut($searchDialog, 'search_close .5s')
    btf.animateOut($searchMask, 'to_hide 0.5s')
    window.removeEventListener('resize', fixSafariHeight)
  }

  const searchClickFn = () => {
    btf.addEventListenerPjax(document.querySelector('#search-button > .search'), 'click', openSearch)
  }

  const searchFnOnce = () => {
    document.querySelector('#local-search .search-close-button').addEventListener('click', closeSearch)
    $searchMask.addEventListener('click', closeSearch)
    if (GLOBAL_CONFIG.localSearch.preload) {
      localSearch.fetchData()
    }
    localSearch.highlightSearchWords(document.getElementById('article-container'))
  }

  window.addEventListener('search:loaded', () => {
    const $loadDataItem = document.getElementById('loading-database')
    $loadDataItem.nextElementSibling.style.display = 'block'
    $loadDataItem.remove()
  })

  searchClickFn()
  searchFnOnce()

  // pjax
  window.addEventListener('pjax:complete', () => {
    !btf.isHidden($searchMask) && closeSearch()
    localSearch.highlightSearchWords(document.getElementById('article-container'))
    searchClickFn()
  })
})

```

