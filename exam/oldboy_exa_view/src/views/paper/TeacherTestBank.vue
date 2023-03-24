<template>
    <div class="box">
        <el-container>
            <el-header height="100px">
                <div class="header pull-left">
                    <div>
                        <i class="el-icon-star-on"></i>
                        题库
                    </div>
                    <div class="header1">
                        <el-button type="primary" size="small" @click="handleCreateTestBank">添加题库</el-button>
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
                            prop="title"
                            label="题库名称"
                            width="180">
                    </el-table-column>
                    <el-table-column
                            label="题数"
                            width="60">
                        <template slot-scope="scope">
                            <span>{{scope.row.subjects_list.length}}</span>
                        </template>
                    </el-table-column>
                    <el-table-column
                            :formatter="dateFormat"
                            prop="date_time"
                            label="创建时间"
                            width="180">
                    </el-table-column>
                    <el-table-column
                            prop="is_commit"
                            label="是否提交"
                            width="100">
                        <template slot-scope="scope">
                            <el-button disabled type="info" size="small" v-if="scope.row.is_commit">已提交</el-button>
                            <el-button type="primary" size="small" v-else @click="handleCommit(scope.row.id)">提交
                            </el-button>
                        </template>
                    </el-table-column>
                    <el-table-column
                            prop="is_start"
                            label="是否开考"
                            width="100">
                        <template slot-scope="scope">
                            <el-button disabled type="info" size="small" v-if="scope.row.is_start">已开考</el-button>
                            <el-button type="primary" size="small" v-else @click="handleStartExam(scope.row.id)">开考
                            </el-button>
                        </template>
                    </el-table-column>
                    <el-table-column
                            prop="is_end"
                            label="是否结束"
                            width="100">
                        <template slot-scope="scope">
                            <span v-if="scope.row.is_end">考试已结束</span>
                            <span v-else>考试未结束</span>
                        </template>
                    </el-table-column>
                    <el-table-column
                            prop="exam_end_time"
                            label="考试截止时间"
                            width="250">
                        <template slot-scope="scope">
                            <span v-if="scope.row.exam_end_time == '1998-10-13T00:00:00'">未设置</span>
                            <span v-else>{{scope.row.exam_end_time}}</span>
                            <span v-if="!(scope.row.is_end || scope.row.is_start)">
                                <i class="el-icon-minus"></i>
                                <el-button type="primary" size="small" @click="handleSetTime(scope.row.id)">
                                    设置
                                </el-button>
                            </span>
                        </template>
                    </el-table-column>
                    <el-table-column
                            align="center"
                            label="操作">
                        <template slot-scope="scope">
                            <el-button type="primary" size="small"
                                       @click="handleRedirect(`/teacherTestBank/testBankView?test_bank_id=${scope.row.id}`)">
                                预览题库
                            </el-button>
                            <el-button type="primary" size="small"
                                       @click="handleChangeName(scope.row.id)">
                                改名
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
        name: "TeacherTestBank",
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
            // if (role_id != '1') {
            //     this.$message({
            //     type: 'warning',
            //     duration: 1000,
            //     message: '你不是老师,没有权限'
            // });
            //     this.$router.go(-1)
            // }
            this.$message({
                type: 'info',
                duration: 500,
                message: '加载数据中'
            });
            this.initialize()
        },
        methods: {
            // 初始化页面
            initialize() {
                // 'http://127.0.0.1:8000/teachers/test-bank/?teachers=2'
                let teachers_id = this.$cookies.get('user_id');
                this.$axios.get(this.$settings.base_url + `teachers/test-bank/?teachers=${teachers_id}&role_id=${this.role_id}`, {headers: {'Authorization': `jwt ${this.token}`}}).then(response => {
                    // console.log(response.data)
                    this.tableData = response.data
                }).catch(error => {
                    console.log(error)
                })
            },

            // 时间格式化
            dateFormat(row, column) {
                // console.log(row, column)
                var date = row[column.property];
                if (date == undefined) {
                    return "";
                }
                return this.$moment(date).format("YYYY年MM月DD日");
            },

            // 跳转到预览题库页面
            handleRedirect(url) {
                this.$router.push(url)
            },

            // 添加题库
            handleCreateTestBank() {
                this.$prompt('请输入题库的名字', '添加题库', {
                    confirmButtonText: '确定',
                    cancelButtonText: '取消',
                }).then(({value}) => {
                    // 'http://127.0.0.1:8000/teachers/test-bank/?teachers=1'
                    this.$axios.post(this.$settings.base_url + `teachers/test-bank/?role_id=${this.role_id}&teachers=${this.teachers_id}`,
                        {
                            'title': value,
                            'teachers': this.teachers_id,
                            'is_commit': false,
                            'is_start': false
                        }, {headers: {'Authorization': `jwt ${this.token}`}}).then(response => {
                        console.log(response)
                        if (response.data.status == 100) {
                            this.$message('成功创建')
                            this.initialize()
                        } else {
                            this.$message('创建失败,可能是缺少什么')
                        }
                    })
                }).catch(() => {
                    this.$message({
                        type: 'info',
                        message: '取消输入',
                        duration: 500
                    });
                });
            },

            // 提交题库
            handleCommit(id) {
                // console.log(id)
                this.$confirm('提交题库后学生可以看到题库, 是否继续?', '提交题库', {
                    confirmButtonText: '确定',
                    cancelButtonText: '取消',
                    type: 'info'
                }).then(() => {
                    // 'http://127.0.0.1:8000/teachers/test-bank/8/?teachers=1'
                    this.$axios.patch(this.$settings.base_url + `teachers/test-bank/${id}/?role_id=${this.role_id}&teachers=${this.teachers_id}`, {
                        'is_commit': true
                    }, {headers: {'Authorization': `jwt ${this.token}`}}).then(response => {
                        console.log(response)
                        if (response.data.status == 100) {
                            this.$message({
                                type: 'success',
                                message: '提交成功!',
                                duration: 1000
                            });
                            this.initialize()
                        } else {
                            this.$message('提交失败')
                        }
                    })
                }).catch(() => {
                    this.$message({
                        type: 'info',
                        message: '已取消提交'
                    });
                });
            },

            // 设置考试截止时间
            handleSetTime(id) {
                this.$prompt('请选择', '设置考试截至时间', {
                    confirmButtonText: '确定',
                    cancelButtonText: '取消',
                    inputType: 'datetime-local',
                    inputPattern: /.+/,
                    inputErrorMessage: '请选择'
                }).then(({value}) => {
                    // console.log(value)
                    // console.log(typeof(value))
                    // 'http://127.0.0.1:8000/teachers/test-bank/8/?teachers=1'
                    this.$axios.patch(this.$settings.base_url + `teachers/test-bank/${id}/?role_id=${this.role_id}&teachers=${this.teachers_id}`, {
                        'exam_end_time': value
                    }, {headers: {'Authorization': `jwt ${this.token}`}}).then(response => {
                        console.log(response)
                        if (response.data.status == 100) {
                            this.$message({
                                type: 'success',
                                message: '设置成功!',
                                duration: 1000
                            });
                            this.initialize()
                        } else {
                            this.$message('设置失败')
                        }
                    })

                }).catch(() => {
                    this.$message({
                        type: 'info',
                        message: '取消设置',
                        duration: 500
                    });
                });
            },

            // 老师开考
            handleStartExam(id) {
                // console.log(id)
                this.$confirm('开始考试后,学生务必在考试截止时间内完成考卷', '开始考试', {
                    confirmButtonText: '确定',
                    cancelButtonText: '取消',
                    type: 'info'
                }).then(() => {
                    // 'http://127.0.0.1:8000/teachers/test-bank/8/?teachers=1'
                    this.$axios.patch(this.$settings.base_url + `teachers/test-bank/${id}/?role_id=${this.role_id}&teachers=${this.teachers_id}`, {
                        'is_start': true
                    }, {headers: {'Authorization': `jwt ${this.token}`}}).then(response => {
                        console.log(response)
                        if (response.data.status == 100) {
                            this.$message({
                                type: 'success',
                                message: '开考成功,提醒学生考试考试!',
                                duration: 1000
                            });
                            this.initialize()
                        } else if (response.data.status == 103) {
                            this.$message('开考失败,没有设置考试时间或者没有提交题库,还有可能是这个题库没有题目')
                        } else this.$message('开考失败')
                    })
                }).catch(() => {
                    this.$message({
                        type: 'info',
                        message: '已取消开考'
                    });
                });
            },

            // 修改题库名称
            handleChangeName(id) {
                this.$prompt('请输入修改后的题库名称', '修改题库名称', {
                    confirmButtonText: '确定',
                    cancelButtonText: '取消',
                    inputPattern: /.+/,
                    inputErrorMessage: '请输入'
                }).then(({value}) => {
                    // 'http://127.0.0.1:8000/teachers/test-bank/8/?teachers=1'
                    this.$axios.patch(this.$settings.base_url + `teachers/test-bank/${id}/?role_id=${this.role_id}&teachers=${this.teachers_id}`, {
                        'title': value
                    }, {headers: {'Authorization': `jwt ${this.token}`}}).then(response => {
                        console.log(response)
                        if (response.data.status == 100) {
                            this.$message({
                                type: 'success',
                                message: '改名成功!',
                                duration: 1000
                            });
                            this.initialize()
                        } else {
                            this.$message('改名失败')
                        }
                    })

                }).catch(() => {
                    this.$message({
                        type: 'info',
                        message: '取消改名',
                        duration: 500
                    });
                });
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

    .header1 {
        margin-top: 15px;
    }
</style>