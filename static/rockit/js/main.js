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
    "jquery": "/static/jquery/dist/jquery.min",
    "domReady": "/static/requirejs-domready/domReady",
    "toastr": "/static/toastr/toastr.min",
  },

  shim: {
    'angular': {
      exports: "angular"
    },
    'jquery': {
      exports: "jquery"
    },
    'angular-translate': {
      deps: ['angular']
    },
    'angular-translate-loader': {
      deps: ['angular-translate']
    },
    'angular-route': {
      deps: ['angular']
    },
    'toastr': {
      exports: "toastr"
    }
  }
});

require(['domReady!', 'angular', 'app'], function (document, ng, app) {
  ng.bootstrap(document, [app.name]);
});