<template>
    <div>
        <SourceNum/>
        <SourceRate/>
    </div>
</template>

<script>
    import SourceRate from "../charts/SourceRate";
    import SourceNum from "../charts/SourceNum";

    export default {
        name: "SourceShow",
        components: {
            SourceNum,
            SourceRate,

        },
        mounted() {

        }
    }
</script>

<style scoped>

</style>