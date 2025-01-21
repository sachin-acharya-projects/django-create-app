from django.core.management.commands.startapp import Command as StartAppCommand
from django.conf import settings
import os


class Command(StartAppCommand):
    def handle(self, *args, **options):
        """
        Handles the creation of a new Django app within the specified directory.

        This method overrides the default handle method to:
        1. Retrieve the default apps directory from Django settings or use "apps" as the default.
        2. Create the apps directory if it does not exist.
        3. Change the current working directory to the apps directory.
        4. Call the parent class's handle method with the provided arguments and options.

        Args:
            *args: Variable length argument list.
            **options: Arbitrary keyword arguments.

        Returns:
            The result of the parent class's handle method.
        """
        apps_dir = str(getattr(settings, "DEFAULT_APP_DIR", "apps"))
        os.makedirs(apps_dir, exist_ok=True)
        os.chdir(apps_dir)
        return super().handle(*args, **options)
