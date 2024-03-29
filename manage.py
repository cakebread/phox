#!/usr/bin/env python

from flask.ext.script import Command, Manager, Shell

from phox import app

manager = Manager(app)


class SyncDB(Command):
    """
    Initializes the database tables.
    """
    def run(self):
        from phox import db
        db.drop_all()
        db.create_all()
        db.session.commit()


class FixedShell(Shell):
    """
    Runs a Python shell inside Flask application context.
    """
    def run(self, no_ipython):
        context = self.get_context()
        if not no_ipython:
            try:
                from IPython.frontend.terminal.embed import InteractiveShellEmbed
                sh = InteractiveShellEmbedbanner1=self.banner
                sh(global_ns=dict(), local_ns=context)
            except ImportError:
                pass
        from code import interact
        interact(banner=self.banner, local=context)


class Test(Command):
    """
    Runs the application's test suite.
    """
    def run(self):
        import os
        from unittest import TestLoader, TextTestRunner
        cur_dir = os.path.dirname(os.path.abspath(__file__))
        loader = TestLoader()
        test_suite = loader.discover(cur_dir)
        runner = TextTestRunner(verbosity=2)
        runner.run(test_suite)


manager._commands['shell'] = FixedShell()
manager.add_command('syncdb', SyncDB())
manager.add_command('test', Test())
manager.run()
