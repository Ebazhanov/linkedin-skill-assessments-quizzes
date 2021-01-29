#### Q1. In WordPress, what is the Loop used to do?

- [ ] It displays a single page.
- [ ] It displays posts on an archive.
- [ ] It displays a single post.
- [x] all of these answers

#### Q2.Who owns the trademark for WordPress and WordCamp names and logos?

- [x] WordPress Foundation (The WordPress Foundation owns and oversees the trademarks for the WordPress and WordCamp names and logos.)
- [ ] WordPress.com
- [ ] Matt Mullenweg
- [ ] Automattic

#### Q3. What is the name of the open-source project that serves as a bug tracker and project management tool for WordPress?

- [ ] HackerOne
- [ ] Redmine
- [x] Trac
- [ ] GitHub Issues

#### Q4. The REST API is a simple way to get data in and out of WordPress over HTTP. Applications using the REST API should be written in which programming language?

- [ ] PHP
- [x] any programming language that can make HTTP requests and interpret JSON
- [ ] Java
- [ ] Node.js

#### Q5. How many minutes does it take to install WordPress according to the "Famous X-Minute Installation" instructions on WordPress.org?

- [x] 5
- [ ] 30
- [ ] 15
- [ ] 10

#### Q6. In WordPress, what is true of plugins?

- [ ] Plugins are available in free or premium (paid) versions.
- [ ] Plugins can extend WordPress core functionality.
- [x] all of these answers
- [ ] Plugins add site-specific features.

#### Q7. Akismet is a plugin that comes automatically installed with WordPress. What does it do?

- [ ] It connects your site to Google Analytics.
- [ ] It displays a blog feed from websites similar to yours.
- [x] It protects your site from comment spam.
- [ ] It hardens site security by enforcing strong passwords.

#### Q8. What would you do to improve your site's performance?

- [ ] Only load scripts and styles on pages where they are needed.
- [ ] Minify CSS and JavaScript files.
- [x] all of these answers
- [ ] Use a CDN.

#### Q9. The REST API utilizes which data format?

- [ ] YAML
- [x] JSON
- [ ] TXT
- [ ] XML

#### Q10. What color is the paragraph nested within the div?

```<html>
<head>
        <style>
                body { color: black; }

                p { color: blue; }

                div { color: green; }

                p { color: red; }
        </style>
</head>
<body>
        <div>
                <p>This is a paragraph inside a div.</p>
        </div>
</body>
</html>
```

- [ ] blue
- [ ] black
- [x] red
- [ ] green

#### Q11. Theme developers can take advantage of the Customizer API to give users a way to manipulate basic theme settings. The Customizer API is object-oriented and provides four main objects. What are they?

- [ ] widgets, containers, sections, settings
- [ ] containers, hooks, settings, styles
- [ ] panels, blocks, controls, settings
- [x] panels, sections, controls, settings

#### Q12. Which WordPress setting would you use to make page URLs look like `http://example.com/my-page/` instead of the default `http://example.com/?p=21/?`

- [ ] Writing
- [x] Permalinks
- [ ] Pretty URLs
- [ ] Reading

#### Q13. In WordPress, what is the block editor used for?

- [ ] cropping images in the media library
- [ ] injecting specialized scripts into the content area
- [x] creating a site layout
- [ ] creating and laying out content

#### Q14. Which of the following file types is NOT involved in translating WordPress?

- [ ] .po
- [x] .pot
- [ ] .mot
- [ ] .mo

#### Q15. What is the default priority for an action hook or filter?

- [x] 10
- [ ] 15
- [ ] 0
- [ ] 5

#### Q16. What's the primary difference between template tags prefaced with the* versus get_the*?

- [ ] Template tags prefaced with the\_ don't accept arguments.
- [ ] Template tags prefaced with the\_ can be used directly within a template.
- [ ] Template tags prefaced with the\_ display a value. Template tags prefaced with get_the return a value.
- [ ] Template tags prefaced with the\_ return a value. Template tags prefaced with get_the display a value.

#### Q17. WP_Query is the WordPress query class that is used to fetch posts from the database. How would you create a new instance of this class?

- [ ] `$query = new query_posts();`
- [x] `$query = new WP_Query();`
- [ ] `$query = query_posts();`
- [ ] `$query = get_posts();`

#### Q18. What is a user role that is unique to WordPress Multisite?

- [ ] MU Admin
- [ ] Owner
- [x] Super Admin
- [ ] Multisite Master

#### Q19. Within the editor, blocks are rendered as JavaScript. How are blocks rendered on the front end of a site?

- [ ] as plain HTML
- [x] as a React component
- [ ] as JavaScript comments
- [ ] as HTML comments

#### Q20. Which of these is NOT a part of the internationalization and localization process?

- [ ] using a gettext function to wrap translatable strings when writing code
- [ ] installing/using the WordPress Multilingual Plugin
- [ ] using a tool like Poedit to parse source code and extract translatable strings into a POT file
- [x] translators translating the POT file into a PO file, one for each language

#### Q21. The REST API provides public data, which is accessible to any client anonymously, as well as private data available only after authentication. How could you ensure that no one can anonymously access site data via the REST API?

- [ ] Disable the REST API via the site's wp-config.php file.
- [ ] Use the `rest_authentication_errors()` filter along with the `is_user_logged_in()` conditional to limit access to logged in users.
- [ ] Use the `rest_authentication_errors()` filter along with cookie authentication to limit access to logged in users.
- [x] Use the Disable REST API plugin.

#### Q22. Which of these snippets represents a wrapper that calls jQuery safely and doesn't require repetitive use of the word "jQuery"?

- [ ] .

```$.ready(function() {
// do stuff
});
```

- [ ] .

```
(function($) {
// do stuff
})( jQuery );
```

- [x] .

```
$(function() {
// do stuff
});
```

- [ ] .

```
jQuery(function($) {
// do stuff
});
```

#### Q23. What is the correct order of parameters for the add_action() function?

- [ ] `add_action( 'example_hook', 'example_function', $accepted_args, $priority )`
- [ ] `add_action( 'example_function', 'example_hook', $priority, $accepted_args )`
- [x] `add_action( 'example_hook', 'example_function', $priority, $accepted_args )`
- [ ] `add_action( 'example_function', 'example_hook', $priority )`

#### Q24. You have a search bar on your site. You would like to use a `<label>` to make the word "Search" visible to screen readers, but you don't want to display the word "Search" on the screen. How can you accomplish this?

- [ ] Assign an ARIA state of "hidden" to the label, like this: `<label state="hidden">Search</label> <input type="text" name="search" id="search" />`
- [x] Use the built-in WordPress CSS class .screen-reader-text to hide the text from screen, like this: `<label class="screen-reader-text">Search</label> <input type="text" name="search" id="search" />`
- [ ] Create a custom CSS class to set a large negative value to the text-indent property to hide the text off screen, like this: `<label class="hide-this">Search</label> <input type="text" name="search" id="search" />`
- [ ] The majority of users do not require a screen reader. Remove the label entirely.

#### Q25. You might see this code in a WordPress plugin. What does it do?

```
if ( ! defined( 'ABSPATH' ) ) {
   die;
}
```

- [ ] This is how WordPress detects a plugin's presence. This ensures that the plugin is running from the /wp-content/plugins/ directory. If it is not, the plugin should not run.
- [x] This is a way to prevent naming collisions. ABSPATH is the absolute path to the plugin's directory. If ABSPATH is defined by another WordPress plugin with the same directory slug, the plugin should not run.
- [ ] This is a security measure. ABSPATH is the absolute path to the WordPress directory. If the file is called directly, ABSPATH will not be defined and therefore the plugin should not run.
- [ ] This is a compatibility checker. ABSPATH is defined in WordPress core. The plugin checks that the minimum version of WordPress needed to support the plugin is installed. If it is not, the plugin should not run.

#### Q26. Which is a best practice for working with WordPress CSS?

- [ ] Use !important next to styles if they don't give you the result you want.
- [ ] Use hyphens in class names.
- [x] Use spaces to indent each property.
- [ ] Avoid CSS shorthand for proper documentation.

#### Q27. WordPress is translated, at least partially, in more than 200 locales. If you wanted to help translate WordPress into other languages, which contributor group would you join?

- [ ] core
- [x] polyglots
- [ ] accessibility
- [ ] documentation

#### Q28. What is the difference between an action and a filter?

- [ ] Actions are used to add custom functions and remove WordPress functions. Filters are used to make strings translatable for localization.
- [x] Actions are used to add or remove code at runtime. Filters are used to modify data before it is either displayed in the browser or saved to the database.
- [ ] Actions are used to assign values to variables at runtime. Filters are used to extract data from actions and display it in the browser.
- [ ] Actions are used to add user-inputted data to the database. Filters are used to validate user-inputted data prior to adding it to the database.

#### Q29. If you activate or update a plugin and it breaks your site so that you cannot manage it via wp-admin, how can you disable the plugin?

- [x] all of these answers
- [ ] Access the WordPress install via WP-CLI. Run the following command: wp plugin deactivate offending-plugin.
- [ ] Access site files via FTP and navigate to /wp-content/plugins/. Delete the folder of the plugin that you would like to disable or simply rename it.
- [ ] Use phpMyAdmin to change the wp_options table's active_plugins option value to a:0:{}.

#### Q30. The WordPress REST API is designed to receive and respond to particular types of requests using basic HTML methods. For example, a request to upload a PHP file into a particular folder on a server might look like the code POST /folder/\_file.php. Based on this code, what would you call /folder/\_file.php (in REST API terms)?

- [ ] schema
- [ ] route
- [ ] response
- [x] request

#### Q31. Which WP-CLI command would you use to manage the capabilities of a user role?

- [ ] wp admin
- [ ] wp manage
- [ ] wp cap
- [x] wp role

#### Q32. What technique would you use to secure data before rendering it to a user?

- [ ] escape and sanitize
- [ ] validate and escape
- [x] validate and sanitize
- [ ] escape and secure

#### Q33. If your WordPress site is seriously compromised, what is the best course of action to return your site to good health?

- [ ] Determine the date of the attack and restore your site to a backup point prior to that date.
- [ ] Hire a third-party service to clean up your site because it is difficult for someone who is not a WordPress security expert to find and remove all traces of an attack.
- [ ] Manually delete suspicious files on the server and delete any database tables that are not core WordPress.
- [ ] Change your hosting password, your WordPress admin password, and your database password.

#### Q34. If you wanted to register a custom post type, which hook would you use?

- [ ] register_post_type
- [ ] add_meta_box
- [ ] wp_head
- [x] init

#### Q35. What is the role of a WordPress theme?

- [ ] controls colors, fonts, and page layouts
- [ ] adds accessibility enhancements such as keyboard navigation and skip links
- [ ] ensures a site is mobile responsive
- [x] all of these answers

#### Q36. What is the name of the open-sourse project that serves as a bug tracker and project management tool for WordPress?

- [ ] Redmine
- [ ] GitHub Issues
- [ ] HakerOne
- [x] Trac

#### Q37. What is a user role that is unique to WordPress Multisite?

- [ ] Owner
- [x] Super Admin
- [ ] MU Admin
- [ ] Multisite Master

### Q38. How would you write a text string containing "Hello World!" in a way that makes it possible for someone else to translate the string into a different language?

- [ ] apply_filters( 'Hello World!', 'mytextdomain' );
- [ ] \_\_( 'Hello World!', 'mytextdomain' );
- [ ] \$string = "Hello World!";
- [ ] esc_html( 'Hello World!', 'mytextdomain' );

### Q39. What is the core mission of WordPress?

- [x] to make free software
- [ ] to democratize publishing and the freedoms that come with open source
- [ ] to make money
- [ ] to encourage blogging

### Q40. Which of the following is NOT a suggested security improvement for your WordPress website?

- [ ] The site should communicate with WordPress.org.
- [ ] Remove inactive themes.
- [ ] Do not output debug information.
- [ ] WordPress updates are accomplished manually only.

### Q41. What's the primary difference between template tags prefaced with the* versus get_the*?

- [ ] Template tags prefaced with the\_ can be used directly within a template. Template tags prefaced with get_the are generally reserved for partial templates.
- [ ] Template tags prefaced with the\_ return a value. Template tags prefaced with get_the display a value.
- [ ] Template tags prefaced with the\_ display a value. Template tags prefaced with get_the return a value.
- [ ] Template tags prefaced with the\_ don't accept arguments. Template tags prefaced with get_the do accept arguments.

### Q42. How can you add a custom script that needs to run only on the contact page of a site? The slug of the page is contact.

Link to the script directly from a template named page-contact.php using the get_header() template tag, like this:
get_header( '<script src="/my-script.js"></script>' );
Use functions.php to conditionally load the script by hooking it to wp_enqueue_scripts(), like this:
add_action( 'wp_enqueue_scripts', 'load_scripts' );

function load_scripts() {
if ( is_page( 'contact' ) ) {
echo '<script src="/my-script.js"></script>';
}
}

Use functions.php to conditionally load the script by hooking it to wp_enqueue_scripts(), like this:
add_action( 'wp_enqueue_scripts', 'load_scripts' );
function load_scripts() {
if ( is_page( 'contact' ) ) {
wp_enqueue_script( 'script', get_template_directory_uri() . '/script.js' );
}
}

- [ ] Link to the script directly from a template named page-contact.php, like this:
- [ ] <head>
- [ ] <script src="/my-script.js"></script>
- [ ] </head>
