define([
  'angular',
  'services',
  'settings/controller'
], function (angular) {
  'use strict';

  return angular.module('rockit.controllers', [
    'rockit.services',
    'rockit.controllers.settings'
  ]);
});