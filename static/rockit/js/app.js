define([
  'angular',
  'directives',
  'routes',
  'services',
  'associations/module',
  'nodes/module',
  'settings/module'], function (ng) {
  'use strict';

  return ng.module("rockit", [
    "rockit.directives",
    "rockit.routes",
    "rockit.services",
    "rockit.associations",
    "rockit.nodes",
    "rockit.settings"
  ]);
});