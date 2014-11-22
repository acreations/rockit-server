'use strict';

require.config({

  /*
   * Base URL for all javascript files
   */
  baseUrl: "/static/rockit/js",

  /*
   * Useful convertings
   */
  maps: {

  },

  paths: {
    "angular": "//ajax.googleapis.com/ajax/libs/angularjs/1.2.26/angular.min",
  },

  shim: {
    angular: {
      exports: "angular"
    }
  }
});

require.config({
  paths: {
    "angular": "/static/angular/angular.min",
  }
});

require(['angular', 'app'], function (angular, app) {
  angular.bootstrap(document, [app.name]);
});