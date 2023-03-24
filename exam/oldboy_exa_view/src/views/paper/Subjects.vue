<template>
    <div class="box">
        <el-container>
            <el-header height="100px">
                <div class="header pull-left">
                    <div>
                        <i class="el-icon-star-on"></i>
                        试题
                    </div>
                    <div class="header1">
                        <el-button type="primary" size="small" @click="dialogFormVisible = true">添加试题</el-button>
                        <el-dialog title="试题信息" :visible.sync="dialogFormVisible">
                            <el-form :model="form">
                                <el-form-item label="试题内容" label-width="120px">
                                    <el-input type="textarea" v-model="form.question" autocomplete="off"></el-input>
                                </el-form-item>
                                <el-form-item label="试题题库" label-width="120px">
                                    <el-select v-model="form.test_bank" placeholder="请选择绑定的题库">
                                        <el-option :label="item.title" :value="item.id"
                                                   v-for="item in this.testBank"></el-option>
                                    </el-select>
                                </el-form-item>
                            </el-form>
                            <div slot="footer" class="dialog-footer">
                                <el-button @click="dialogFormVisible = false">取 消</el-button>
                                <el-button type="primary" @click="handleCreateSubjects">确 定</el-button>
                            </div>
                        </el-dialog>
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
                            prop="subject_status"
                            label="题目类型"
                            width="100">
                    </el-table-column>
                    <el-table-column
                            prop="teachers_name"
                            label="出题老师"
                            width="100">
                    </el-table-column>
                    <el-table-column
                            prop="test_bank_name"
                            label="题库名"
                            width="180">
                    </el-table-column>
                    <el-table-column
                            prop="test_bank_is_start"
                            label="是否开考"
                            width="100">
                        <template slot-scope="scope">
                            <span v-if="scope.row.test_bank_is_start">已开考</span>
                            <span v-else>未开考</span>
                        </template>
                    </el-table-column>
                    <el-table-column
                            align="center"
                            label="操作">
                        <template slot-scope="scope">
                            <span v-if="!scope.row.test_bank_is_start">
                                <el-button type="primary" size="small"
                                           @click="handleDeleteSubject(scope.row.id)">删除试题</el-button>
                                <el-button type="primary" size="small"
                                           @click="handleSetSubject(scope.row.id, scope.row.question, scope.row.test_bank)">修改试题</el-button>
                            </span>
                            <span>
                                &nbsp
                                <el-button type="primary" size="small"
                                           @click="handleShowSubject(scope.row.question)">预览试题</el-button>
                            </span>
<!--                            <el-button type="info" size="small" v-else disabled>题库已开考,无法操作</el-button>-->
                        </template>
                    </el-table-column>
                </el-table>
            </el-main>
        </el-container>
    </div>
</template>

<script>
    export default {
        name: "Subjects",
        data() {
            return {
                tableData: [],
                testBank: [],
                teachers_id: Number(this.$cookies.get('user_id')),
                role_id: this.$cookies.get('role_id'),
                token: this.$cookies.get('token'),

                dialogFormVisible: false,
                form: {
                    question: '',
                    test_bank: ''
                },
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
            initialize() {
                // 'http://127.0.0.1:8000/teachers/subjects/?teachers=1'
                this.$axios.get(this.$settings.base_url + `teachers/subjects/?teachers=${this.teachers_id}&role_id=${this.role_id}`, {
                    headers: {'Authorization': `jwt ${this.token}`}
                }).then(response => {
                    // console.log(response.data)
                    this.tableData = response.data
                }).catch(error => {
                    console.log(error)
                })

                // 'http://127.0.0.1:8000/teachers/get_teachers_test_bank/?teachers=1'
                this.$axios.get(this.$settings.base_url + `teachers/get_teachers_test_bank/?teachers=${this.teachers_id}&role_id=${this.role_id}`, {
                    headers: {'Authorization': `jwt ${this.token}`}
                }).then(response => {
                    // console.log(response.data)
                    this.testBank = response.data
                }).catch(error => {
                    console.log(error)
                })
            },

            // 添加试题
            handleCreateSubjects() {
                this.dialogFormVisible = false;
                // console.log(this.form.question)
                // console.log(this.form.test_bank)
                // 'http://127.0.0.1:8000/teachers/subjects/?teachers=1'
                this.$axios.post(this.$settings.base_url + `teachers/subjects/?teachers=${this.teachers_id}&role_id=${this.role_id}`, {
                    'question': this.form.question,
                    'test_bank': this.form.test_bank,
                    'teachers': this.teachers_id
                }, {
                    headers: {'Authorization': `jwt ${this.token}`}
                }).then(response => {
                    // console.log(response.data)
                    if (response.data.status == 100) {
                        this.$message({
                            type: 'success',
                            message: '添加成功',
                            duration: 1000
                        });
                        this.initialize()
                    } else {
                        this.$message({
                            type: 'error',
                            message: response.data.msg,
                            duration: 1000
                        })
                    }
                }).catch(error => {
                    console.log(error)
                })
            },

            // 预览试题
            handleShowSubject(content) {
                this.$alert(content, '试题内容', {
                    confirmButtonText: '确定',
                });
            },

            // 修改试题
            handleSetSubject(id, content, test_bank_id) {
                this.$prompt('请修改', '修改试题', {
                    confirmButtonText: '确定',
                    cancelButtonText: '取消',
                    inputPattern: /.+/,
                    inputErrorMessage: '不能为空',
                    inputValue: content,
                    inputType: 'textarea'
                }).then(({value}) => {
                    // 'http://127.0.0.1:8000/teachers/subjects/12/?teachers=1'
                    this.$axios.patch(this.$settings.base_url + `teachers/subjects/${id}/?teachers=${this.teachers_id}&role_id=${this.role_id}`, {
                        'question': value,
                        'teachers': this.teachers_id,
                        'test_bank': test_bank_id
                    }, {
                        headers: {'Authorization': `jwt ${this.token}`}
                    }).then(response => {
                        // console.log(response.data)
                        if (response.data.status == 100) {
                            this.$message({
                                type: 'success',
                                message: '修改成功!',
                                duration: 1000,
                            });
                            this.initialize()
                        } else this.$message(response.data.msg)
                    })
                }).catch(() => {
                    this.$message({
                        type: 'info',
                        message: '取消修改',
                        duration: 1000,
                    });
                });
            },

            // 删除试题
            handleDeleteSubject(id) {
                this.$confirm('此操作将永久删除该试题, 是否继续?', '提示', {
                    confirmButtonText: '确定',
                    cancelButtonText: '取消',
                    type: 'warning'
                }).then(() => {
                    // 'http://127.0.0.1:8000/teachers/subjects/9/?teachers=1'  delete
                    this.$axios.delete(this.$settings.base_url + `teachers/subjects/${id}/?teachers=${this.teachers_id}&role_id=${this.role_id}`, {
                        headers: {'Authorization': `jwt ${this.token}`}
                    }).then(response => {
                        // console.log(response.data)
                        this.$message({
                            type: 'success',
                            message: '删除成功!',
                            duration: 1000,
                        });
                        this.initialize()
                    }).catch(error => {
                        console.log(error)
                    })
                }).catch(() => {
                    this.$message({
                        type: 'info',
                        message: '已取消删除',
                        duration: 1000,
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