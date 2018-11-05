def get_or_none(model, *args, **kwargs):
	""" Helper function for Model.object.get() """

	try:
		return model.objects.get(*args, **kwargs)
	except model.DoesNotExist:
		return None