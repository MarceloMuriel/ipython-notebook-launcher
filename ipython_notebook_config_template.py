# Configuration file for ipython-notebook.

c = get_config()

#------------------------------------------------------------------------------
# NotebookApp configuration
#------------------------------------------------------------------------------

# NotebookApp will inherit config from: BaseIPythonApplication, Application

# The date format used by logging formatters for %(asctime)s
# c.NotebookApp.log_datefmt = '%Y-%m-%d %H:%M:%S'

# Hashed password to use for web authentication.
# 
# To generate, type in a python/IPython shell:
# 
#   from IPython.lib import passwd; passwd()
# 
# The string should be of the form type:salt:hashed-password.
# c.NotebookApp.password = ''

# Whether to open in a browser after starting. The specific browser used is
# platform dependent and determined by the python standard library `webbrowser`
# module, unless it is overridden using the --browser (NotebookApp.browser)
# configuration option.
# c.NotebookApp.open_browser = True

# The base URL for the websocket server, if it differs from the HTTP server
# (hint: it almost certainly doesn't).
# 
# Should be in the form of an HTTP origin: ws[s]://hostname[:port]
# c.NotebookApp.websocket_url = ''

# Wether to use Browser Side less-css parsing instead of compiled css version in
# templates that allows it. This is mainly convenient when working on the less
# file to avoid a build step, or if user want to overwrite some of the less
# variables without having to recompile everything.
# 
# You will need to install the less.js component in the static directory either
# in the source tree or in your profile folder.
# c.NotebookApp.use_less = False

# Set the log level by value or name.
# c.NotebookApp.log_level = 30

# Whether to trust or not X-Scheme/X-Forwarded-Proto and X-Real-Ip/X-Forwarded-
# For headerssent by the upstream reverse proxy. Neccesary if the proxy handles
# SSL
# c.NotebookApp.trust_xheaders = False

# The url for MathJax.js.
# c.NotebookApp.mathjax_url = ''

# The name of the IPython directory. This directory is used for logging
# configuration (through profiles), history storage, etc. The default is usually
# $HOME/.ipython. This options can also be specified through the environment
# variable IPYTHONDIR.
# c.NotebookApp.ipython_dir = '/var/imi/prog/.ipython'

# The notebook manager class to use.
# c.NotebookApp.notebook_manager_class = 'IPython.html.services.notebooks.filenbmanager.FileNotebookManager'

# Create a massive crash report when IPython encounters what may be an internal
# error.  The default is to append a short message to the usual traceback
# c.NotebookApp.verbose_crash = False

# The full path to a private key file for usage with SSL/TLS.
# c.NotebookApp.keyfile = ''

# The port the notebook server will listen on.
# c.NotebookApp.port = 8888

# The random bytes used to secure cookies. By default this is a new random
# number every time you start the Notebook. Set it to a value in a config file
# to enable logins to persist across server sessions.
# 
# Note: Cookie secrets should be kept private, do not share config files with
# cookie_secret stored in plaintext (you can read the value from a file).
# c.NotebookApp.cookie_secret = b''

# Extra paths to search for serving static files.
# 
# This allows adding javascript/css to be available from the notebook server
# machine, or overriding individual files in the IPython
# c.NotebookApp.extra_static_paths = []

# The base URL for the kernel server
# 
# Leading and trailing slashes can be omitted, and will automatically be added.
# c.NotebookApp.base_kernel_url = '/'

# The Logging format template
# c.NotebookApp.log_format = '[%(name)s]%(highlevel)s %(message)s'

# The IPython profile to use.
# c.NotebookApp.profile = 'default'

# The IP address the notebook server will listen on.
# c.NotebookApp.ip = '127.0.0.1'

# Whether to install the default config files into the profile dir. If a new
# profile is being created, and IPython contains config files for that profile,
# then they will be staged into the new directory.  Otherwise, default config
# files will be automatically generated.
# c.NotebookApp.copy_config_files = False

# Whether to overwrite existing config files when copying
# c.NotebookApp.overwrite = False

# The base URL for the notebook server.
# 
# Leading and trailing slashes can be omitted, and will automatically be added.
# c.NotebookApp.base_project_url = '/'

# Whether to enable MathJax for typesetting math/TeX
# 
# MathJax is the javascript library IPython uses to render math/LaTeX. It is
# very large, so you may want to disable it if you have a slow internet
# connection, or for offline use of the notebook.
# 
# When disabled, equations etc. will appear as their untransformed TeX source.
# c.NotebookApp.enable_mathjax = True

# Supply overrides for the tornado.web.Application that the IPython notebook
# uses.
# c.NotebookApp.webapp_settings = {}

# The full path to an SSL/TLS certificate file.
# c.NotebookApp.certfile = ''

# The number of additional ports to try if the specified port is not available.
# c.NotebookApp.port_retries = 50

# Specify what command to use to invoke a web browser when opening the notebook.
# If not specified, the default browser will be determined by the `webbrowser`
# standard library module, which allows setting of the BROWSER environment
# variable to override it.
# c.NotebookApp.browser = ''

# Path to an extra config file to load.
# 
# If specified, load this config file in addition to any other IPython config.
# c.NotebookApp.extra_config_file = ''

#------------------------------------------------------------------------------
# IPKernelApp configuration
#------------------------------------------------------------------------------

# IPython: an enhanced interactive Python shell.

# IPKernelApp will inherit config from: BaseIPythonApplication, Application,
# InteractiveShellApp

# set the shell (ROUTER) port [default: random]
# c.IPKernelApp.shell_port = 0

# The date format used by logging formatters for %(asctime)s
# c.IPKernelApp.log_datefmt = '%Y-%m-%d %H:%M:%S'

# A file to be run
# c.IPKernelApp.file_to_run = ''

# A list of dotted module names of IPython extensions to load.
# c.IPKernelApp.extensions = []

# ONLY USED ON WINDOWS Interrupt this process when the parent is signaled.
# c.IPKernelApp.interrupt = 0

# List of files to run at IPython startup.
# c.IPKernelApp.exec_files = []

# Enable GUI event loop integration with any of ('glut', 'gtk', 'gtk3', 'none',
# 'osx', 'pyglet', 'qt', 'qt4', 'tk', 'wx').
# c.IPKernelApp.gui = None

# Whether to create profile dir if it doesn't exist
# c.IPKernelApp.auto_create = False

# Run the module as a script.
# c.IPKernelApp.module_to_run = ''

# kill this process if its parent dies.  On Windows, the argument specifies the
# HANDLE of the parent process, otherwise it is simply boolean.
# c.IPKernelApp.parent_handle = 0

# The importstring for the DisplayHook factory
# c.IPKernelApp.displayhook_class = 'IPython.kernel.zmq.displayhook.ZMQDisplayHook'

# Create a massive crash report when IPython encounters what may be an internal
# error.  The default is to append a short message to the usual traceback
# c.IPKernelApp.verbose_crash = False

# lines of code to run at IPython startup.
# c.IPKernelApp.exec_lines = []

# The importstring for the OutStream factory
# c.IPKernelApp.outstream_class = 'IPython.kernel.zmq.iostream.OutStream'

# redirect stderr to the null device
# c.IPKernelApp.no_stderr = False

# set the heartbeat port [default: random]
# c.IPKernelApp.hb_port = 0

# Set the log level by value or name.
# c.IPKernelApp.log_level = 30

# If true, IPython will populate the user namespace with numpy, pylab, etc. and
# an 'import *' is done from numpy and pylab, when using pylab mode.
# 
# When False, pylab mode should not import any names into the user namespace.
# c.IPKernelApp.pylab_import_all = True

# 
# c.IPKernelApp.parent_appname = ''

# The name of the IPython directory. This directory is used for logging
# configuration (through profiles), history storage, etc. The default is usually
# $HOME/.ipython. This options can also be specified through the environment
# variable IPYTHONDIR.
# c.IPKernelApp.ipython_dir = '/var/imi/prog/.ipython'

# The Kernel subclass to be used.
# 
# This should allow easy re-use of the IPKernelApp entry point to configure and
# launch kernels other than IPython's own.
# c.IPKernelApp.kernel_class = 'IPython.kernel.zmq.ipkernel.Kernel'

# Configure matplotlib for interactive use with the default matplotlib backend.
# c.IPKernelApp.matplotlib = None

# Pre-load matplotlib and numpy for interactive use, selecting a particular
# matplotlib backend and loop integration.
# c.IPKernelApp.pylab = None

# The Logging format template
# c.IPKernelApp.log_format = '[%(name)s]%(highlevel)s %(message)s'

# The IPython profile to use.
# c.IPKernelApp.profile = 'default'

# Set the IP or interface on which the kernel will listen.
# c.IPKernelApp.ip = ''

# JSON file in which to store connection info [default: kernel-<pid>.json]
# 
# This file will contain the IP, ports, and authentication key needed to connect
# clients to this kernel. By default, this file will be created in the security
# dir of the current profile, but can be specified by absolute path.
# c.IPKernelApp.connection_file = ''

# Whether to install the default config files into the profile dir. If a new
# profile is being created, and IPython contains config files for that profile,
# then they will be staged into the new directory.  Otherwise, default config
# files will be automatically generated.
# c.IPKernelApp.copy_config_files = False

# Whether to overwrite existing config files when copying
# c.IPKernelApp.overwrite = False

# set the control (ROUTER) port [default: random]
# c.IPKernelApp.control_port = 0

# Execute the given command string.
# c.IPKernelApp.code_to_run = ''

# redirect stdout to the null device
# c.IPKernelApp.no_stdout = False

# 
# c.IPKernelApp.transport = 'tcp'

# set the iopub (PUB) port [default: random]
# c.IPKernelApp.iopub_port = 0

# Path to an extra config file to load.
# 
# If specified, load this config file in addition to any other IPython config.
# c.IPKernelApp.extra_config_file = ''

# set the stdin (ROUTER) port [default: random]
# c.IPKernelApp.stdin_port = 0

# dotted module name of an IPython extension to load.
# c.IPKernelApp.extra_extension = ''

#------------------------------------------------------------------------------
# ZMQInteractiveShell configuration
#------------------------------------------------------------------------------

# A subclass of InteractiveShell for ZMQ.

# ZMQInteractiveShell will inherit config from: InteractiveShell

# Deprecated, use PromptManager.in2_template
# c.ZMQInteractiveShell.prompt_in2 = '   .\\D.: '

# Enable magic commands to be called without the leading %.
# c.ZMQInteractiveShell.automagic = True

# Use colors for displaying information about objects. Because this information
# is passed through a pager (like 'less'), and some pagers get confused with
# color codes, this capability can be turned off.
# c.ZMQInteractiveShell.color_info = True

# Set the size of the output cache.  The default is 1000, you can change it
# permanently in your config file.  Setting it to 0 completely disables the
# caching system, and the minimum value accepted is 20 (if you provide a value
# less than 20, it is reset to 0 and a warning is issued).  This limit is
# defined because otherwise you'll spend more time re-flushing a too small cache
# than working
# c.ZMQInteractiveShell.cache_size = 1000

# Save multi-line entries as one entry in readline history
# c.ZMQInteractiveShell.multiline_history = True

# 
# c.ZMQInteractiveShell.xmode = 'Context'

# 
# c.ZMQInteractiveShell.readline_remove_delims = '-/~'

# 'all', 'last', 'last_expr' or 'none', specifying which nodes should be run
# interactively (displaying output from expressions).
# c.ZMQInteractiveShell.ast_node_interactivity = 'last_expr'

# Deprecated, use PromptManager.in_template
# c.ZMQInteractiveShell.prompt_in1 = 'In [\\#]: '

# 
# c.ZMQInteractiveShell.separate_out = ''

# 
# c.ZMQInteractiveShell.quiet = False

# Start logging to the given file in append mode.
# c.ZMQInteractiveShell.logappend = ''

# 
# c.ZMQInteractiveShell.wildcards_case_sensitive = True

# Deprecated, use PromptManager.justify
# c.ZMQInteractiveShell.prompts_pad_left = True

# A list of ast.NodeTransformer subclass instances, which will be applied to
# user input before code is run.
# c.ZMQInteractiveShell.ast_transformers = []

# 
# c.ZMQInteractiveShell.ipython_dir = ''

# 
# c.ZMQInteractiveShell.separate_out2 = ''

# Automatically call the pdb debugger after every exception.
# c.ZMQInteractiveShell.pdb = False

# 
# c.ZMQInteractiveShell.readline_parse_and_bind = ['tab: complete', '"\\C-l": clear-screen', 'set show-all-if-ambiguous on', '"\\C-o": tab-insert', '"\\C-r": reverse-search-history', '"\\C-s": forward-search-history', '"\\C-p": history-search-backward', '"\\C-n": history-search-forward', '"\\e[A": history-search-backward', '"\\e[B": history-search-forward', '"\\C-k": kill-line', '"\\C-u": unix-line-discard']

# Start logging to the default log file.
# c.ZMQInteractiveShell.logstart = False

# 
# c.ZMQInteractiveShell.debug = False

# 
# c.ZMQInteractiveShell.object_info_string_level = 0

# Show rewritten input, e.g. for autocall.
# c.ZMQInteractiveShell.show_rewritten_input = True

# 
# c.ZMQInteractiveShell.separate_in = '\n'

# Don't call post-execute functions that have failed in the past.
# c.ZMQInteractiveShell.disable_failing_post_execute = False

# Make IPython automatically call any callable object even if you didn't type
# explicit parentheses. For example, 'str 43' becomes 'str(43)' automatically.
# The value can be '0' to disable the feature, '1' for 'smart' autocall, where
# it is not applied if there are no more arguments on the line, and '2' for
# 'full' autocall, where all callable objects are automatically called (even if
# no arguments are present).
# c.ZMQInteractiveShell.autocall = 0

# Enable deep (recursive) reloading by default. IPython can use the deep_reload
# module which reloads changes in modules recursively (it replaces the reload()
# function, so you don't need to change anything to use it). deep_reload()
# forces a full reload of modules whose code may have changed, which the default
# reload() function does not.  When deep_reload is off, IPython will use the
# normal reload(), but deep_reload will still be available as dreload().
# c.ZMQInteractiveShell.deep_reload = False

# Deprecated, use PromptManager.out_template
# c.ZMQInteractiveShell.prompt_out = 'Out[\\#]: '

# The name of the logfile to use.
# c.ZMQInteractiveShell.logfile = ''

# Set the color scheme (NoColor, Linux, or LightBG).
# c.ZMQInteractiveShell.colors = 'Linux'

# 
# c.ZMQInteractiveShell.history_length = 10000

#------------------------------------------------------------------------------
# KernelManager configuration
#------------------------------------------------------------------------------

# Manages a single kernel in a subprocess on this host.
# 
# This version starts kernels with Popen.

# KernelManager will inherit config from: ConnectionFileMixin

# The Popen Command to launch the kernel. Override this if you have a custom
# c.KernelManager.kernel_cmd = []

# Should we autorestart the kernel if it dies.
# c.KernelManager.autorestart = False

# 
# c.KernelManager.transport = 'tcp'

# Set the kernel's IP address [default localhost]. If the IP address is
# something other than localhost, then Consoles on other machines will be able
# to connect to the Kernel, so be careful!
# c.KernelManager.ip = '127.0.0.1'

#------------------------------------------------------------------------------
# ProfileDir configuration
#------------------------------------------------------------------------------

# An object to manage the profile directory and its resources.
# 
# The profile directory is used by all IPython applications, to manage
# configuration, logging and security.
# 
# This object knows how to find, create and manage these directories. This
# should be used by any code that wants to handle profiles.

# Set the profile location directly. This overrides the logic used by the
# `profile` option.
# c.ProfileDir.location = ''

#------------------------------------------------------------------------------
# Session configuration
#------------------------------------------------------------------------------

# Object for handling serialization and sending of messages.
# 
# The Session object handles building messages and sending them with ZMQ sockets
# or ZMQStream objects.  Objects can communicate with each other over the
# network via Session objects, and only need to work with the dict-based IPython
# message spec. The Session will handle serialization/deserialization, security,
# and metadata.
# 
# Sessions support configurable serialiization via packer/unpacker traits, and
# signing with HMAC digests via the key/keyfile traits.
# 
# Parameters ----------
# 
# debug : bool
#     whether to trigger extra debugging statements
# packer/unpacker : str : 'json', 'pickle' or import_string
#     importstrings for methods to serialize message parts.  If just
#     'json' or 'pickle', predefined JSON and pickle packers will be used.
#     Otherwise, the entire importstring must be used.
# 
#     The functions must accept at least valid JSON input, and output *bytes*.
# 
#     For example, to use msgpack:
#     packer = 'msgpack.packb', unpacker='msgpack.unpackb'
# pack/unpack : callables
#     You can also set the pack/unpack callables for serialization directly.
# session : bytes
#     the ID of this Session object.  The default is to generate a new UUID.
# username : unicode
#     username added to message headers.  The default is to ask the OS.
# key : bytes
#     The key used to initialize an HMAC signature.  If unset, messages
#     will not be signed or checked.
# keyfile : filepath
#     The file containing a key.  If this is set, `key` will be initialized
#     to the contents of the file.

# Threshold (in bytes) beyond which an object's buffer should be extracted to
# avoid pickling.
# c.Session.buffer_threshold = 1024

# The UUID identifying this session.
# c.Session.session = ''

# The maximum number of digests to remember.
# 
# The digest history will be culled when it exceeds this value.
# c.Session.digest_history_size = 65536

# The name of the packer for serializing messages. Should be one of 'json',
# 'pickle', or an import name for a custom callable serializer.
# c.Session.packer = 'json'

# Threshold (in bytes) beyond which a buffer should be sent without copying.
# c.Session.copy_threshold = 65536

# Metadata dictionary, which serves as the default top-level metadata dict for
# each message.
# c.Session.metadata = {}

# Username for the Session. Default is your system username.
# c.Session.username = 'imiprog'

# execution key, for extra authentication.
# c.Session.key = b''

# The maximum number of items for a container to be introspected for custom
# serialization. Containers larger than this are pickled outright.
# c.Session.item_threshold = 64

# Debug output in the Session
# c.Session.debug = False

# The name of the unpacker for unserializing messages. Only used with custom
# functions for `packer`.
# c.Session.unpacker = 'json'

# The digest scheme used to construct the message signatures. Must have the form
# 'hmac-HASH'.
# c.Session.signature_scheme = 'hmac-sha256'

# path to file containing execution key.
# c.Session.keyfile = ''

#------------------------------------------------------------------------------
# MappingKernelManager configuration
#------------------------------------------------------------------------------

# A KernelManager that handles notebook mapping and HTTP error handling

# MappingKernelManager will inherit config from: MultiKernelManager

# The kernel manager class.  This is configurable to allow subclassing of the
# KernelManager for customized behavior.
# c.MappingKernelManager.kernel_manager_class = 'IPython.kernel.ioloop.IOLoopKernelManager'

#------------------------------------------------------------------------------
# NotebookManager configuration
#------------------------------------------------------------------------------

# The directory to use for notebooks.
# c.NotebookManager.notebook_dir = '/var/imi/prog'

#------------------------------------------------------------------------------
# FileNotebookManager configuration
#------------------------------------------------------------------------------

# FileNotebookManager will inherit config from: NotebookManager

# The location in which to keep notebook checkpoints
# 
# By default, it is notebook-dir/.ipynb_checkpoints
# c.FileNotebookManager.checkpoint_dir = ''

# The directory to use for notebooks.
# c.FileNotebookManager.notebook_dir = '/var/imi/prog'

# Automatically create a Python script when saving the notebook.
# 
# For easier use of import, %run and %load across notebooks, a <notebook-
# name>.py script will be created next to any <notebook-name>.ipynb on each
# save.  This can also be set with the short `--script` flag.
# c.FileNotebookManager.save_script = False
