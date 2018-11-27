import warnings

try:
    from simple_recipes.version import version as __version__
except:
    warnings.warn("Could not import version, has simple_recipes been installed?")