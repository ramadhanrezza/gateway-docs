Contributing
############

.. toctree::
   :includehidden:
   :maxdepth: 6

Guidelines
**********

Project Organization
====================

- Clone from ``master`` branch.
- Should create new branch for bug fixing or feature and merged into ``master`` when completed.

Repository Naming
=================

- feature-<yourfeaturename> if your project is a new feature.
- bug-<yourbugname> if your project is fixing bug.

Submitting Pull Request
=======================

- Make sure to create unit test based on your code.
- commit and push your new branch based on Repository Naming Guidlines.
- Update ``CHANGELOG`` if there is a new pluggin need to install.
- Submit new pull request to ``master`` branch.

Standards
*********

Commit Message Standard
=======================

Use these pattern for commit message::

 Add: <your commit message>
 Update: <your commit message>
 Remove: <your commit message>
 Fix: <your commit message>

Code Standard
=============

Follow `PSR-2 <https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-2-coding-style-guide.md>`_ coding standard and the `PSR-4 <https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-4-autoloader.md>`_ autoloading standard.


PHPDoc
======

Below is example of valid documentation block::

 /**
 * Register a binding with the container.
 *
 * @param  string|array  $abstract
 * @param  \Closure|string|null  $concrete
 * @param  bool  $shared
 * @return void
 *
 * @throws \Exception
 */
 public function bind($abstract, $concrete = null, $shared = false)
 {
 	//
 }

Project Structure
=================

Backend Project (ex: Gateway Service)
-------------------------------------

  Use standard Lumen Project Structure::

   |- app
      |- Http
         |- Controllers
            |- NewController.php 
         |- Middleware
            |- NewMiddleware.php
      |- NewModel.php
   |- bootstrap
      |- app.php
   |- config
      |- database.php
      |- logging.php
   |- database
      |- migrations
         |- yourtablemigrations.php
      |- seeds
         |- yourtableseeds.php
   |- public
   |- resources
   |- routes
      |- web.php
   |- storage
   |- tests
      |- YourControllerTest.php
   |- .env
   |- services.yml (only for gateway service)
   |- CHANGELOG.md

Frontend Project (ex: Dashboard)
--------------------------------

 Use standard Laravel Project Structure::

  |- app
     |- Http
        |- Controllers
           |- Dashboard
              |- YourController.php
           |- Demography
              |- YourController.php
        |- Middleware
           |- YourMiddleware.php
  |- bootstrap
  |- config
  |- database
  |- public
     |- css
        |- dashboard
           |- yourcss.css
        |- demography
           |- yourcss.css
     |- js
        |- dashboard
           |- yourjs.js
        |- demography
           |- yourjs.js
  |- resources
     |- views
        |- dashboard
           |- layout
              |- yourlayout.blade.php
           yoursection.blade.php
        |- demography
           |- layout
              |- yourlayout.blade.php
           yoursection.blade.php
  |- routes
     |- web.php
  |- storage
  |- tests
     |- YourControllerTest.php
  |- .env
  |- CHANGELOG.md

LOG Format
====================