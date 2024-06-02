const path = require('path');

module.exports = {
  mode: 'production',
  entry: './static/scripts.js',
  output: {
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'dist'),
  },
  resolve: {
    alias: {
      '@3d-dice/dice-box': path.resolve(__dirname, 'node_modules/@3d-dice/dice-box/dist/dice-box.es.js'),
    },
  },
};
