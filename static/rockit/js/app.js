define([
  'angular',
  'configs',
  'services',
  'associations/controller',
  'nodes/controller',
  'settings/controller'], function (angular) {
  'use strict';

  return angular.module("rockit", [
    "rockit.services",
    "rockit.associations",
    "rockit.nodes",
    "rockit.settings",
  ]);
});