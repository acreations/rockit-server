define([
  'angular',
  'configs',
  'directives',
  'services',
  'associations/controller',
  'nodes/controller',
  'settings/controller'], function (angular) {
  'use strict';

  return angular.module("rockit", [
    "rockit.directives",
    "rockit.services",
    "rockit.associations",
    "rockit.nodes",
    "rockit.settings",
  ]);
});