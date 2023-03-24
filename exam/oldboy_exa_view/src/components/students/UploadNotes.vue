<template>
    <div>
        <hr>
        <h1 style="font-size: xx-large; font-weight: bold; margin-top: 50px">笔记上传</h1>
        <div style="width: 400px; margin: auto">
            <el-upload
                    class="upload-demo"
                    drag
                    style="margin-top: 130px"
                    action="http://127.0.0.1:8000/upload/"
                    :before-upload="beforeUpload"
                    multiple
                    accept=".md,.txt,.doc,.docx,.ppt,.pdf"
                    :on-success="open1"
                    :on-error="open2"
            >
                <i class="el-icon-upload"></i>
                <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
                <div class="el-upload__tip" slot="tip">只能上传 md、txt、doc、docx、ppt、pdf文件，且不超过2M</div>
            </el-upload>
        </div>
        <hr style="margin-top: 100px">
    </div>
</template>

<script>
    export default {
        name: "UploadNotes",
        data() {
            return {
                formData: [],
                errormsg: '',
                succssmsg: '',
            }
        },
        methods: {
            beforeUpload(file) {
                var fileSuffix = file.name.substring(file.name.lastIndexOf(".") + 1);
                var whiteList = ["md", "txt", "doc", "docx", "ppt", "pdf"];
                var isLt2M = file.size / 1024 / 1024 < 2;

                if (this.formData.length == 0) {
                    this.formData = new FormData();
                } else if (whiteList.indexOf(fileSuffix) === -1) {
                    this.errormsg = "上传文件只能是 md、txt、doc、docx、ppt格式"
                    this.open3()
                    return false;
                } else if (!isLt2M) {
                    this.errormsg = "上传文件大小不能超过 2MB"
                    this.open3()
                    return false;
                } else {
                    this.formData.append('file', file.file);
                    this.onSubmit()
                }

            },
            onSubmit() {
                let headers = {
                    headers: {
                        "Content-Type": "multipart/form-data"
                    }
                }
                this.$axios.post(`${this.$settings.base_url}upload/`, this.formData, headers)
                    .then((res) => {
                        console.log(res)
                        if (res.data.status == 100) {
                            this.succssmsg = res.data.data_all
                            this.open1()
                        } else {
                            this.errormsg = res.data.data_all
                            this.open3()
                        }
                    })
                    .catch(() => {
                        this.open2()
                    });
            },
            open1() {
                this.$notify({
                    title: '成功',
                    message: this.succssmsg,
                    type: 'success'
                });
            },
            open2() {
                this.$notify.error({
                    title: '错误',
                    message: "上传失败",
                });
            },
            open3() {
                this.$notify.error({
                    title: '错误',
                    message: this.errormsg,
                });
            },
        }
    }
</script>

<style scoped>

</style>