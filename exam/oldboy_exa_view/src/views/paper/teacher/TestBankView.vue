<template>
    <div class="container">
        <div class="row header">
            <span>预览题库</span>
            <span>考试截止时间{{data.exam_end_time}}</span>
        </div>
        <div class="row content" v-for="(item, index) in data.subjects_list">
            <span>{{index+1}}、{{item.question}}</span>
        </div>
        <div class="footer">
            <el-button type="primary" size="small" @click="handleGoBack">返回上一页面</el-button>
        </div>
    </div>
</template>

<script>
    export default {
        name: "TestBankView",
        data() {
            return {
                data: {},
                teachers_id: Number(this.$cookies.get('user_id')),
                role_id: this.$cookies.get('role_id'),
                token: this.$cookies.get('token'),
            }
        },
        mounted() {
            // 权限校验
            // let role_id = this.$cookies.get('role_id')
            // if (role_id != '1') {
            //     this.$message({
            //     type: 'warning',
            //     duration: 1000,
            //     message: '你不是老师,没有权限'
            // });
            //     this.$router.go(-1)
            // }

            // 获得问号后面的值
            // console.log(this.$route.query)
            let test_bank_id = this.$route.query.test_bank_id
            let teachers_id = this.$cookies.get('user_id')
            // console.log(test_bank_id)
            // 问号后面的不在path中
            // console.log(this.$route.path)

            // 'http://127.0.0.1:8000/teachers/test-bank/1/?teachers=1'
            this.$axios.get(this.$settings.base_url + `teachers/test-bank/${test_bank_id}/?teachers=${teachers_id}&role_id=${this.role_id}`, {
                headers: {'Authorization': `jwt ${this.token}`}
            }).then(response => {
                // console.log(response.data)
                this.data = response.data
            }).catch(error => {
                console.log(error)
            })
        },
        methods: {
            handleGoBack() {
                this.$router.go(-1)
            }
        },
    }
</script>

<style scoped>
    .header {
        font-weight: bold;
        font-size: 30px;
    }

    .content {
        font-size: 20px;
        margin-top: 10px;
    }

    .footer {
        margin-top: 10px;
    }
</style>