define(['angular'], function (angular) {
  'use strict';

  var module = angular.module('rockit.configs', []);

  return module.factory('settings', function () {

    var server = '//localhost';

    return {
      'serverUrl': server + '/rockit',

    };
  });
});