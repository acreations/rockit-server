define([
  'angular',
  'configs',
  'controllers'], function (angular) {
  'use strict';

  return angular.module("rockit", ["rockit.configs", "rockit.controllers"]);
});