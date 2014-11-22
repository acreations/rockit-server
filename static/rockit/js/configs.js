define(['angular'], function (angular) {
  'use strict';

  var module = angular.module('rockit.configs', []);

  return module.factory('settings', function () {

    var server = '//localhost:8000';

    return {
      'serverUrl': server + '/api/rockit',
    };
  });
});