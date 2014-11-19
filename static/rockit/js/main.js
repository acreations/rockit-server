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
    },
  }

});

require(['angular', 'app', function (angular) {
  angular.bootstrap(document.documentElement, ["rockit"]);
}]);