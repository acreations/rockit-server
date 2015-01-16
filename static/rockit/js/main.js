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
    "angular-resource": "/static/angular-resource/angular-resource.min",
    "angular-translate": "/static/angular-translate/angular-translate.min",
    "angular-translate-loader": "/static/angular-translate-loader-partial/angular-translate-loader-partial.min",
    "clockpicker": "/static/clockpicker/dist/jquery-clockpicker.min",
    "jquery": "/static/jquery/dist/jquery.min",
    "domReady": "/static/requirejs-domready/domReady",
    "selecter": "/static/Selecter/jquery.fs.selecter",
    "toastr": "/static/toastr/toastr.min",
  },

  shim: {
    'angular': {
      exports: "angular"
    },
    'angular-route': {
      deps: ['angular']
    },
    'angular-resource': {
      deps: ['angular']
    },
    'angular-translate': {
      deps: ['angular']
    },
    'angular-translate-loader': {
      deps: ['angular-translate']
    },
    'clockpicker': {
      deps: ['jquery']
    },
    'jquery': {
      exports: "jquery"
    },
    'selecter': {
      deps: ['jquery']
    },
    'toastr': {
      exports: "toastr"
    }
  }
});

require(['domReady!', 'angular', 'app', 'angular-resource'], function (document, ng, app) {
  ng.bootstrap(document, [app.name]);
});