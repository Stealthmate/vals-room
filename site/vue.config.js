module.exports = {
  publicPath: process.env.NODE_ENV === 'production'
    ? '/vals-room/'
    : '/',
  transpileDependencies: [
    'vuetify'
  ]
}
