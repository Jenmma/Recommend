<template>
  <div class="home">
    <el-menu
      class="menu"
      :router="true"
      :default-active="defaultActive"
      background-color="#545c64"
      text-color="#fff"
      active-text-color="#ffd04b">
      <el-menu-item index="/menu1" route="/home/menu1">
        <i class="el-icon-menu"></i>
        <span slot="title">导航一</span>
      </el-menu-item>
      <el-menu-item index="/menu2" route="/home/menu2">
        <i class="el-icon-user"></i>
        <span slot="title">导航二</span>
      </el-menu-item>
      <el-menu-item index="/menu3" route="/home/menu3">
        <i class="el-icon-document"></i>
        <span slot="title">导航三</span>
      </el-menu-item>
      <el-menu-item index="/menu4" route="/home/menu4">
        <i class="el-icon-setting"></i>
        <span slot="title">导航四</span>
      </el-menu-item>
    </el-menu>
    <router-view style="padding-left:200px;"/>
  </div>
</template>

<script>
// @ is an alias to  /src

export default {
  name: "Home",
  methods: {
  },
  computed: {
    defaultActive() {
      console.log('/' + this.$route.path.split('/').reverse()[0])
      return '/' + this.$route.path.split('/').reverse()[0];
        
    }
  }
};
</script>

<style scoped>
.menu{
  width: 200px;
  min-height: 714px;
  position:absolute;
}
</style>
