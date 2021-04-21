<template>
  <div class="about">
    <h1>新闻相关数据统计</h1>
    {{getdata()}}
    <bingzhuangtu class="bing" ref="mychild2"/>//饼状图
    <Echarts class="Echarts1" ref="mychild" />//柱状图
  </div>
</template>

<script>
import Echarts from "../components/menu1/Echarts";
import {get} from "../router/request";
import Bingzhuangtu from "../components/menu1/bingzhuangtu";
export default {
  name:"First",
  components: {Bingzhuangtu, Echarts},
  data(){
    return{
      msg:"Welcome to 推荐系统",
      input: "",
    };
  },
  methods: {
    getdata() {
      get({
        url: "/api/test",
      })
          .then((res) => {
            if (res.data.ok == 1) {
              //调用函数
              this.$refs.mychild.drawLine(res.data.data.title)
              this.$refs.mychild2.initData(res.data.data.abstract)
            }
          })
    },

  },
}
</script>
<style scoped>
.about{
  position:absolute;
  top:-10px;
  left:200px;
}
.Echarts1 {
  margin-top: 220px;
  display: flex;
  justify-content:left;
}
</style>