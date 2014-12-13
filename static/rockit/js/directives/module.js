/**
 * Module for handle nodes
 */
define(['angular',
  './input/editable',
  './navigation/breadcrumb',
  './navigation/navbar'], function (ng, editable, breadcrumb, navbar) {
  'use strict';

  var module = ng.module("rockit.directives", []);

  return module
    .directive('breadcrumb', breadcrumb)
    .directive('editable', editable)
    .directive('navbar', navbar);

});