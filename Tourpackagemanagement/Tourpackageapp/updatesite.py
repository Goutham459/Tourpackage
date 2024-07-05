from django.contrib.sites.models import Site

# Create or retrieve the Site object
site = Site.objects.get_or_create(id=1)[0]

# Update site attributes
site.domain = 'http://127.0.0.1:8000/'
site.name = 'http://127.0.0.1:8000/'

# Save the changes
site.save()

# Print the site ID
print(site.id)
