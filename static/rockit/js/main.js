'use strict';

require.config({

  /*
   * Base URL for all javascript files
   */
  baseUrl: "/static/rockit/js",

  /*
   * Useful convertings
   */
  map: {
    "settings/service": "mock"
  },

  paths: {
    "angular": "/static/angular/angular.min",
    "angular-route": "/static/angular-route/angular-route.min",
    "angular-translate": "/static/angular-translate/angular-translate.min",
    "angular-translate-loader": "/static/angular-translate-loader-partial/angular-translate-loader-partial.min",
    "domReady": "/static/requirejs-domready/domReady"
  },

  shim: {
    'angular': {
      exports: "angular"
    },
    'angular-translate': {
      deps: ['angular']
    },
    'angular-translate-loader': {
      deps: ['angular-translate']
    },
    'angular-route': {
      deps: ['angular']
    }
  }
});

require(['domReady!', 'angular', 'app'], function (document, ng, app) {
  ng.bootstrap(document, [app.name]);
});