const _global: any = global || window;

_global.WebSocket = _global.WebSocket || require('ws');
_global.Blob = _global.Blob || require('fetch-blob');