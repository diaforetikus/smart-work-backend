import{_ as v,o,c as b,a as i,w as s,n,d as u}from"./index-c3548e4f.js";const c={props:["jobs","owner"],emits:["changed"],data(){return{jobStatus:null}},methods:{setStatus(l){this.jobStatus=l,this.$emit("changed",l)}}},S={class:"flex space-x-4 ml-10","aria-label":"Tabs"};function f(l,t,m,k,e,a){return o(),b("nav",S,[i("a",{href:"#",onClick:t[0]||(t[0]=s(r=>a.setStatus(null),["prevent"])),class:n(e.jobStatus===null?"main-tab-active":"main-tab")},"All",2),m.owner?(o(),b("a",{key:0,href:"#",onClick:t[1]||(t[1]=s(r=>a.setStatus(1),["prevent"])),class:n(e.jobStatus===1?"main-tab-active":"main-tab")},"Open",2)):u("",!0),i("a",{href:"#",onClick:t[2]||(t[2]=s(r=>a.setStatus(2),["prevent"])),class:n(e.jobStatus===2?"main-tab-active":"main-tab")},"Waiting",2),i("a",{href:"#",onClick:t[3]||(t[3]=s(r=>a.setStatus(3),["prevent"])),class:n(e.jobStatus===3?"main-tab-active":"main-tab")},"At work",2),i("a",{href:"#",onClick:t[4]||(t[4]=s(r=>a.setStatus(4),["prevent"])),class:n(e.jobStatus===4?"main-tab-active":"main-tab")},"Completed",2),m.owner?(o(),b("a",{key:1,href:"#",onClick:t[5]||(t[5]=s(r=>a.setStatus(5),["prevent"])),class:n(e.jobStatus===5?"main-tab-active":"main-tab")},"Canceled",2)):u("",!0)])}const j=v(c,[["render",f]]);export{j as T};
