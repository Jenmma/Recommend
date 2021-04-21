<template>
  <div id="menu1Demo">
    <el-input
      v-model="input"
      placeholder="请输入内容"
      prefix-icon="el-icon-search"
      @change="onSearch()"
    />
    <relation-chart class="relation-chart" ref="mychild" />
  </div>
</template>

<script>
import RelationChart from "../components/menu1/RelationChart.vue";
// import relation from "../components/json/relation.json";
import {get} from "../router/request.js"
export default {
  name: "menu1Demo",
  data() {
    return {
      input: "",
      draw: false,
    };
  },
  components: {
    RelationChart,
  },
  methods: {
    onSearch() {
      console.log(this.input);
      get({
        url: "/api/relationchart",
        params: {
          userid: this.input,
        },
      })

        .then((res) => {
          console.log(res)
          console.log("what's this?")
          if (res.data.ok == 1) {
            console.log(res.data.data)
            this.$refs.mychild.drawChart(res.data.data)
          }
        })
      
    },
  },
  computed: {
    defaultActive() {
      console.log("/" + this.$route.path.split("/").reverse()[0]);
      return "/" + this.$route.path.split("/").reverse()[0];
    },
  },
};
</script>

<style scoped>
>>> div.el-input {
  width: 550px;
  top: 100px;
}
>>> input.el-input__inner {
  border-width: 0px;
  border-radius: 20px;
  box-shadow: 0px 0px 5px #c0c0c0;
}

.relation-chart {
  margin-top: 220px;
  display: flex;
  justify-content: center;
}
</style>