#### Q1. In WordPress, what is the Loop used to do?
- [ ] It displays a single page.
- [ ] It displays posts on an archive.
- [ ] It displays a single post.
- [X] all of these answers

#### Q2.Who owns the trademark for WordPress and WordCamp names and logos?
- [X] WordPress Foundation (The WordPress Foundation owns and oversees the trademarks for the WordPress and WordCamp names and logos.)
- [ ] WordPress.com
- [ ] Matt Mullenweg
- [ ] Automattic

#### Q3. 
- [ ] HackerOne
- [ ] Redmine
- [ ] Trac
- [ ] GitHub Issues

#### Q4. The REST API is a simple way to get data in and out of WordPress over HTTP. Applications using the REST API should be written in which programming language?
- [ ] PHP
- [X] any programming language that can make HTTP requests and interpret JSON
- [ ] Java
- [ ] Node.js

#### Q5. How many minutes does it take to install WordPress according to the "Famous X-Minute Installation" instructions on WordPress.org?
- [X] 5
- [ ] 30
- [ ] 15
- [ ] 10

#### Q6. In WordPress, what is true of plugins?
- [ ] Plugins are available in free or premium (paid) versions.
- [ ] Plugins can extend WordPress core functionality.
- [X] all of these answers
- [ ] Plugins add site-specific features.

#### Q7. Akismet is a plugin that comes automatically installed with WordPress. What does it do?
- [ ] It connects your site to Google Analytics.
- [ ] It displays a blog feed from websites similar to yours.
- [X] It protects your site from comment spam.
- [ ] It hardens site security by enforcing strong passwords.

#### Q8. What would you do to improve your site's performance?
- [ ] Only load scripts and styles on pages where they are needed.
- [ ] Minify CSS and JavaScript files.
- [X] all of these answers
- [ ] Use a CDN.

#### Q9. The REST API utilizes which data format?
- [ ] YAML
- [X] JSON
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
- [X] red
- [ ] green

#### Q11. Theme developers can take advantage of the Customizer API to give users a way to manipulate basic theme settings. The Customizer API is object-oriented and provides four main objects. What are they?
- [ ] widgets, containers, sections, settings
- [ ] containers, hooks, settings, styles
- [ ] panels, blocks, controls, settings
- [ ] panels, sections, controls, settings

#### Q12. Which WordPress setting would you use to make page URLs look like `http://example.com/my-page/` instead of the default `http://example.com/?p=21/?`
- [ ] Writing
- [X] Permalinks
- [ ] Pretty URLs
- [ ] Reading

#### Q13. In WordPress, what is the block editor used for?
- [ ] cropping images in the media library
- [ ] injecting specialized scripts into the content area
- [X] creating a site layout
- [ ] creating and laying out content

#### Q14. Which of the following file types is NOT involved in translating WordPress?
- [ ] .po
- [X] .pot
- [ ] .mot
- [ ] .mo

#### Q15. What is the default priority for an action hook or filter?
- [X] 10
- [ ] 15
- [ ] 0
- [ ] 5

#### Q16. What's the primary difference between template tags prefaced with the_ versus get_the_?
- [ ] Template tags prefaced with the_ don't accept arguments.
- [ ] Template tags prefaced with the_ can be used directly within a template.
- [ ] Template tags prefaced with the_ display a value. Template tags prefaced with get_the return a value.
- [ ] Template tags prefaced with the_ return a value. Template tags prefaced with get_the display a value.

#### Q17. WP_Query is the WordPress query class that is used to fetch posts from the database. How would you create a new instance of this class?
- [ ] `$query = new query_posts();`
- [ ] `$query = new WP_Query();`
- [ ] `$query = query_posts();`
- [ ] `$query = get_posts();`

#### Q18. What is a user role that is unique to WordPress Multisite?
- [ ] MU Admin
- [ ] Owner
- [ ] Super Admin
- [ ] Multisite Master

#### Q19. Within the editor, blocks are rendered as JavaScript. How are blocks rendered on the front end of a site?Within the editor, blocks are rendered as JavaScript. How are blocks rendered on the front end of a site?
- [ ] as plain HTML
- [ ] as a React component
- [ ] as JavaScript comments
- [ ] as HTML comments

#### Q20. Which of these is NOT a part of the internationalization and localization process?
- [ ] using a gettext function to wrap translatable strings when writing code
- [ ] installing/using the WordPress Multilingual Plugin
- [ ] using a tool like Poedit to parse source code and extract translatable strings into a POT file
- [ ] translators translating the POT file into a PO file, one for each language

#### Q21. The REST API provides public data, which is accessible to any client anonymously, as well as private data available only after authentication. How could you ensure that no one can anonymously access site data via the REST API?
- [ ] Disable the REST API via the site's wp-config.php file.
- [ ] Use the `rest_authentication_errors()` filter along with the `is_user_logged_in()` conditional to limit access to logged in users.
- [ ] Use the `rest_authentication_errors()` filter along with cookie authentication to limit access to logged in users.
- [ ] Use the Disable REST API plugin.

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
        
- [ ] .
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
- [ ] `add_action( 'example_hook', 'example_function', $priority, $accepted_args )`
- [ ] `add_action( 'example_function', 'example_hook', $priority )`

#### Q24. You have a search bar on your site. You would like to use a `<label>` to make the word "Search" visible to screen readers, but you don't want to display the word "Search" on the screen. How can you accomplish this?
- [ ] Assign an ARIA state of "hidden" to the label, like this: `<label state="hidden">Search</label> <input type="text" name="search" id="search" />`
- [ ] Use the built-in WordPress CSS class .screen-reader-text to hide the text from screen, like this: `<label class="screen-reader-text">Search</label> <input type="text" name="search" id="search" />`
- [ ] Create a custom CSS class to set a large negative value to the text-indent property to hide the text off screen, like this: `<label class="hide-this">Search</label> <input type="text" name="search" id="search" />`
- [ ] The majority of users do not require a screen reader. Remove the label entirely.

#### Q25. You might see this code in a WordPress plugin. What does it do?
```
if ( ! defined( 'ABSPATH' ) ) {
   die;
}
```
- [ ] This is how WordPress detects a plugin's presence. This ensures that the plugin is running from the /wp-content/plugins/ directory. If it is not, the plugin should not run.
- [ ] This is a way to prevent naming collisions. ABSPATH is the absolute path to the plugin's directory. If ABSPATH is defined by another WordPress plugin with the same directory slug, the plugin should not run.
- [ ] This is a security measure. ABSPATH is the absolute path to the WordPress directory. If the file is called directly, ABSPATH will not be defined and therefore the plugin should not run.
- [ ] This is a compatibility checker. ABSPATH is defined in WordPress core. The plugin checks that the minimum version of WordPress needed to support the plugin is installed. If it is not, the plugin should not run.

#### Q26. Which is a best practice for working with WordPress CSS?
- [ ] Use !important next to styles if they don't give you the result you want.
- [ ] Use hyphens in class names.
- [ ] Use spaces to indent each property.
- [ ] Avoid CSS shorthand for proper documentation.

#### Q27. WordPress is translated, at least partially, in more than 200 locales. If you wanted to help translate WordPress into other languages, which contributor group would you join?
- [ ] core
- [ ] polyglots
- [ ] accessibility
- [ ] documentation

#### Q28. What is the difference between an action and a filter?
- [ ] Actions are used to add custom functions and remove WordPress functions. Filters are used to make strings translatable for localization.
- [ ] Actions are used to add or remove code at runtime. Filters are used to modify data before it is either displayed in the browser or saved to the database.
- [ ] Actions are used to assign values to variables at runtime. Filters are used to extract data from actions and display it in the browser.
- [ ] Actions are used to add user-inputted data to the database. Filters are used to validate user-inputted data prior to adding it to the database.

#### Q29. If you activate or update a plugin and it breaks your site so that you cannot manage it via wp-admin, how can you disable the plugin?
- [X] all of these answers
- [ ] Access the WordPress install via WP-CLI. Run the following command: wp plugin deactivate offending-plugin.
- [ ] Access site files via FTP and navigate to /wp-content/plugins/. Delete the folder of the plugin that you would like to disable or simply rename it.
- [ ] Use phpMyAdmin to change the wp_options table's active_plugins option value to a:0:{}.



#### Q30. The WordPress REST API is designed to receive and respond to particular types of requests using basic HTML methods. For example, a request to upload a PHP file into a particular folder on a server might look like the code POST /folder/_file.php. Based on this code, what would you call /folder/_file.php (in REST API terms)?
- [ ] schema
- [ ] route
- [ ] response
- [ ] request
