module.exports = {
    module: {
        rules: [{
            test: /\.js$/,
            exclude: /node_mudules/,
            use: {
                loader: "babel-loader"
            }
        }]
    }
}