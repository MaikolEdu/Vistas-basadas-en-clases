from django.db import models
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
from django.db.models.signals import post_init
from django.dispatch import receiver




class Entry(models.Model):
	'''
	La clase Publicacion recibira como entradas un titulo ..
	'''
	title		=	models.CharField(max_length=50, unique=True, db_index=True)
	content		=	models.TextField()
	slug		=	models.SlugField(max_length=100,editable=False)
	created_date=	models.DateTimeField(auto_now_add=True,editable=False)
	updated_date=	models.DateTimeField(auto_now=True,editable=False)

	def get_absolute_url(self):
		return reverse("entry_detail",kwargs={'slug':self.slug})

	def save(self,*args,**kwargs):
		if not self.id:
			self.slug=slugify(self.title)
			super(Entry,self).save(*args,**kwargs)

	def __unicode__(self):
		return self.title

	@receiver(post_init)
	def capitalizeTitle(sender,**kwargs):
		instance=kwargs['instance']
		instance.title=instance.title.capitalize()
		kwargs['instance'] = instance