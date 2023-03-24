<template>
    <div class="box">
        <el-container>
            <el-header height="50px">
                <div class="header pull-left">
                    <div>
                        <i class="el-icon-star-on"></i>
                        考卷
                    </div>
                </div>
            </el-header>
            <el-main>
                <el-table
                        :data="tableData"
                        border
                        style="width: 100%">
                    <el-table-column
                            align="center"
                            type="index"
                            label="序号"
                            width="50">
                        <template slot-scope="scope">
                            <span>{{scope.$index+1}}</span>
                        </template>
                    </el-table-column>
                    <el-table-column
                            prop="test_bank_name"
                            label="题库名"
                            width="180">
                    </el-table-column>
                    <el-table-column
                            align="center"
                            label="题数"
                            width="50">
                        <template slot-scope="scope">
                            <span>{{scope.row.subjects_list.length}}</span>
                        </template>
                    </el-table-column>
                    <el-table-column
                            prop="teachers_name"
                            label="出题老师"
                            width="100">
                    </el-table-column>
                    <el-table-column
                            :formatter="dateFormat"
                            prop="commit_time"
                            label="提交时间"
                            width="200">
                    </el-table-column>
                    <el-table-column
                            align="center"
                            label="修改考卷"
                            width="130">
                        <template slot-scope="scope">
                            <el-button disabled type="info" size="small" v-if="scope.row.test_bank_is_end">
                                考试已结束
                            </el-button>
                            <el-button type="primary" size="small" v-else
                                       @click="handleRedirect(`/studentTestBank/setPaperView?paper_id=${scope.row.id}`)">
                                修改
                            </el-button>
                        </template>
                    </el-table-column>
                    <el-table-column
                            align="center"
                            label="是否批改"
                            width="100">
                        <template slot-scope="scope">
                            <span v-if="scope.row.is_check">是</span>
                            <span v-else>否</span>
                        </template>
                    </el-table-column>
                    <el-table-column
                            align="center"
                            label="操作">
                        <template slot-scope="scope">
                            <el-button type="primary" size="small"
                                       @click="handleRedirect(`/studentTestBank/paperView?paper_id=${scope.row.id}`)">
                                预览考卷
                            </el-button>
                        </template>
                    </el-table-column>
                </el-table>
            </el-main>
        </el-container>
    </div>
</template>

<script>
    export default {
        name: "StudentPaper",
        data() {
            return {
                tableData: [],
                teachers_id: Number(this.$cookies.get('user_id')),
                role_id: this.$cookies.get('role_id'),
                token: this.$cookies.get('token'),
            }
        },
        mounted() {
            // 权限校验
            // let role_id = this.$cookies.get('role_id')
            // if (role_id != '2') {
            //     this.$message({
            //     type: 'warning',
            //     duration: 1000,
            //     message: '你不是学生,没有权限'
            // });
            //     this.$router.go(-1)
            // }
            this.$message({
                type: 'info',
                duration: 500,
                message: '加载数据中'
            });
            // 'http://127.0.0.1:8000/students/student-paper/?student_id=1'
            let students_id = this.$cookies.get('user_id');
            this.$axios.get(this.$settings.base_url + `students/student-paper/?student_id=${students_id}&role_id=${this.role_id}`, {
                headers: {'Authorization': `jwt ${this.token}`}
            }).then(response => {
                // console.log(response.data)
                this.tableData = response.data
            }).catch(error => {
                console.log(error)
            })
        },
        methods: {
            // 时间格式化
            dateFormat(row, column) {
                // console.log(row, column)
                var date = row[column.property];
                if (date == undefined) {
                    return "";
                }
                return this.$moment(date).format("YYYY年MM月DD日 HH:mm:ss");
            },

            // 跳转到预览考卷和修改考卷页面
            handleRedirect(url) {
                this.$router.push(url)
            },

        },
    }
</script>

<style scoped>
    .box {
        height: 100%;
        box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1)
    }

    .header {
        font-size: 20px;
        font-weight: normal;
        margin-top: 20px;
    }
</style>