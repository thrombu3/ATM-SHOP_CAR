// 导入jquery写入
const webpack = require("webpack");
module.exports = {
    // 导入jquery写入
    configureWebpack: {
        plugins: [
            new webpack.ProvidePlugin({
                $: "jquery",
                jQuery: "jquery",
                "window.jQuery": "jquery",
                "window.$": "jquery",
                Popper: ["popper.js", "default"]
            })
        ]
    },
    devServer: {
        port: 8080,
        proxy: {
            '/test': {
                target: 'http://127.0.0.1:8000/',
            },
        },
    }
};
