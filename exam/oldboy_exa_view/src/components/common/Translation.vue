<template>
    <div class="translation">
        <div class="a" v-show="isShows" @click="trans">
            <section class="remind1">
                <span style="font-weight: bold; font-size: large; color: #878484;">点我翻译</span>
            </section>
        </div>


        <div class="b" v-show="issShows">
            <section id="trans" class="remind2">
                <span style="font-weight: bold; font-size: large; text-align: right; margin-top: 4px; color: black" @click="transs"> x </span>
                <span style="font-weight: bold; font-size: large; text-align: left; margin-top: 4px; display:inline">翻译: </span>
                <br>
                <el-input
                        class="inline-input"
                        v-model="disease"
                        placeholder="请输入您要搜索单词或句子"
                        @keyup.enter.native="search"
                ></el-input>
            </section>
            <el-button slot="reference" style="display: none"></el-button>
        </div>

    </div>
</template>

<script>
    export default {
        name: "Translation",
        data() {
            return {
                isShows: true,
                issShows: false,
                diseaseAnswer: '', //这个值是需要匹配的值
                disease: ''     //这个值是用户正在输入的值
            }
        },
        mounted() {

        },
        methods: {
            search() {
                if (!this.disease) {
                    this.$message.warning('请输入您要搜索单词或短语!')
                } else {
                    this.$axios.post(`${this.$settings.base_url}translation/`, {
                        disease: this.disease
                    }).then(res => {
                        if (res.data.status == 100) {
                            this.diseaseAnswer = res.data.data_all
                            this.open()
                        } else if (res.data.status == 102) {
                            this.$message.warning(res.data.msg)
                        } else {
                            this.diseaseAnswer = res.data.data_all
                            this.$message.warning('请输入正确单词或短语!')
                        }
                    }).catch(() => {
                        this.$message.info('后端错误!')
                    })
                }
            },
            trans() {
                this.isShows = false
                this.issShows = true
            },
            transs() {
                this.isShows = true
                this.issShows = false
            },
            open() {
                this.$alert(this.diseaseAnswer, '翻译结果: ', {
                    confirmButtonText: '确定',
                })
            }
        },
    }
</script>

<style scoped>
    .remind1 {
        border-radius: 2px;
        padding: 10px 10px;
        display: flex;
        position: fixed;
        right: 20px;
        bottom: 70%;
        flex-direction: column;
        color: #606266;
        background-color: #fcf9f9;
        border-left: 4px solid #7ff2fd;
        box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
    }

    .remind2 {
        width: 600px;
        border-radius: 2px;
        padding: 10px 10px;
        display: flex;
        position: fixed;
        right: 10px;
        bottom: 70%;
        flex-direction: column;
        color: #606266;
        background-color: #fcf9f9;
        border-left: 4px solid #7ff2fd;
        box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
    }

</style>