# django-flags

Django app that allows your users to flag spam/offensive objects in your model.

## Installation

- Add `flags` folder to Python path.
- Add `"flags"` to your `INSTALLED_APPS`.
- Add the following pattern to your urlconf:


    ```
    from flags import urls as flags_urls    
    
    urlpatterns = [
        # ...
        url(r'^flags/', include(flags_urls, namespace='flags')),
    ]
    ```

## Usage

### Flagging an object

In order to let your users flag an object, use a templatetag:


    {% load flags %}
    
    <a href="{% flag_create_url my_object %}">Report abuse</a>

### Admin panel

You can moderate flagged objects through Django admin panel. There are two actions available - you can decide either to delete flagged object or to approve it.

After you approve an object, there is no way to flag it again - all users reports will be silenced.

### Custom template

You probably want to customize `templates/flags/flag_form.html` file to make it consistent with the rest of your site.

### Auto-deleting objects

You can also specify a number of flags which is enough to delete an object automatically. To do that, simply add to your settings the following line:


    FLAGS_THRESHOLD = 10
    

## Demo

`django-flags` provides a simple demo with example usage. To install it from the console, execute `fab install` command. To run it, type ``fab runserver``.

Of course, to do that you need to have `fabric` installed on your computer.

## Tests

Tests assume that Selenium's ChromeDriver can be found at:
> /usr/bin/chromedriver

It also needs correct permissions. Make sure to run:

    $ sudo chmod a+x /usr/bin/chromedriver

To run all the tests simply type:

    $ fab install
    $ fab testall

## Notes

This package was tested with Python 3.4 and Django 1.8.

## License

MIT

