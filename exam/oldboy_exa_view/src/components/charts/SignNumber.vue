<template>
    <div id="main" style="width: 1260px;height:450px;"></div>

</template>

<script>
    export default {
        name: "SignNumber",
        methods: {
            getDateAndsetTest() {
                let sign_num_l = []
                let no_sign_num_l = []
                let sign_date = []
                this.$axios.get(`${this.$settings.base_url}students/get_sign_detail_all/`
                ).then(response => {
                    if (response.data.status == 100) {
                        for (var i = 0; i < response.data.data_all.length; i++) {
                            sign_num_l.push(response.data.data_all[i].sign_number);
                            no_sign_num_l.push(response.data.data_all[i].no_sign_number);
                            sign_date.push(response.data.data_all[i].date_time);
                        }
                        this.signData(sign_date, sign_num_l, no_sign_num_l)
                    }
                }).catch(() => {
                    this.$message({
                        message: '后端错误!'
                    });
                })
            },
            signData(sign_date, sign_num_l, no_sign_num_l) {
                var myChart = this.$echarts.init(document.getElementById('main'));
                var option = {
                    title: {
                        text: '学员签到数据',
                        subtext: '数据来自于近一周'
                    },
                    tooltip: {
                        trigger: 'axis',
                        axisPointer: {
                            type: 'shadow'
                        }
                    },
                    legend: {

                        data: ['签到数', '未签到数']
                    },
                    grid: {
                        left: '3%',
                        right: '4%',
                        bottom: '3%',
                        containLabel: true
                    },
                    xAxis: {
                        type: 'value',
                        boundaryGap: [0, 0.01]
                    },
                    yAxis: {
                        type: 'category',
                        data: sign_date
                    },
                    series: [
                        {
                            name: '签到数',
                            type: 'bar',
                            data: sign_num_l,
                        },
                        {
                            name: '未签到数',
                            type: 'bar',
                            data: no_sign_num_l,
                        }
                    ]
                };

                myChart.setOption(option);
            },
        },
        mounted() {
            this.getDateAndsetTest();
        },
    }
</script>

<style scoped>

</style>