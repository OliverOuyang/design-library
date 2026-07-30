/* 运行时唯一库存真源：预览页从此清单派生分类、数量、路径与标签。 */
const INTEGRITY = {
  "音效/按压/click1.wav":"dd90b97f38b0ec7d52161d7c3bf8d61a66655766fd0af06439963351b4853a83", "音效/按压/click2.wav":"a8b35cb35ff45738a9d7fe008490ad21a3ad30417dadd544a435d8b0ea84d841", "音效/按压/click3.wav":"8d0676a5bcbfedad3e65b7b73e93a044216d7f192c99a3a05caf21e2aa4a8dda", "音效/按压/click4.wav":"0d80e2c82426316b140b0686e10f83924ef794e9a9dfe13aaaa794b18200b048", "音效/按压/click5.wav":"8a6f69fef5d241794a98d0b71baf0c7f51743c9e54ee4dd010a0323a8edeca83",
  "音效/悬停/rollover1.wav":"97de1348d22990014d9b5da4a2dedb6a070b324bb5966f7b4819eafa616b4a0c", "音效/悬停/rollover2.wav":"c0c10c006967920edbb29ca364099a42ad3459a823d75f18a90181ac36774bf2", "音效/悬停/rollover3.wav":"f3a9e0cf97fd20c963d3793a42fc26a8f137b11d916cce1aca10b6419521eaa3", "音效/悬停/rollover4.wav":"7f00105fea3df85ae1b348152169e02485c8565ace881be5fc6f88d6282764c7", "音效/悬停/rollover5.wav":"12da6d7c42d0e6bfcc04e68e5d61c6a8605fbb8c27f662abbf1d376a564ff114",
  "音效/切换/switch1.wav":"e48f397e7dffafab68a2252287b8ff0e3805f141f76e51a3c6285e72e0d443d0", "音效/切换/switch2.wav":"b0f7b256b9baa6ff7558c2d7404d29754671939627b9ae27cc49b5d558721170", "音效/切换/switch3.wav":"2c04718535a175affda107adc8cad34abdccc94b9a9100297e39a0077c207515", "音效/切换/switch4.wav":"83956adf4ac68a44a7ab6d7f69d03560a3e575fa1cc11431fe291f859f2178a9", "音效/切换/switch5.wav":"824feeb7f534127a82dd41bffc63613b59a412940b173aad9e6165a904cb05b3",
  "动效/进入与层级/01-柔和上浮.html":"274b83802bc5e0164348d960fc94c9e6241a9bfbb3e873ca8ac22068f88a25ff", "动效/进入与层级/02-左右揭示.html":"bdb1f67cea7bbff8a4c745e2bc7bdc515e2637d754345a547656933ffce7b1e6", "动效/进入与层级/03-焦点缩放.html":"cba0115c82aa912826ec55790dbe8cc913b1756269c21947f40df79067ed957e", "动效/进入与层级/04-叠层展开.html":"285d59189277eb5857650bcf9236503e473c4cb08c8ea6797a7c6ce9398aa5cc", "动效/进入与层级/05-阶梯入场.html":"e14b87fb7955f8ae66cedf4e0e0e376550d573dbf17cba19be89f420fa06fad2",
  "动效/加载与等待/01-轨道循环.html":"fb24daef981560dcea0ea5b8addb3ffda6cb4f76e8ea07e0d97e1260318b3b8e", "动效/加载与等待/02-呼吸点.html":"2a286d7f7a05af472a40fc7b535a4cb3a680d1a51479f49981d33abf2191cc33", "动效/加载与等待/03-节奏省略号.html":"d220e5f6c9c6e98059132cad732f7bfedeb8e3f33663fa8d24ba64f45e086a0f", "动效/加载与等待/04-扫描线.html":"d721d414555d7e2459bbef60bbd5e2647a93e646d243774c00bf40ceeda5ffa8", "动效/加载与等待/05-进度填充.html":"1e521e377e34fd57075942dd2808294e0918eae58b9a454f5b272611e600aa99",
  "动效/状态反馈/01-成功收束.html":"af4529415379fb35514cbdbcccd145925c235ee2d96f2f88867d0262b919610c", "动效/状态反馈/02-错误回弹.html":"83d6d1594e1baa7f824745044b0103cd2e2615e4db473e078115ee591433cf62", "动效/状态反馈/03-提示波纹.html":"4aec6473623afdc6d38bacd3a3281a95777dd798041bae5f027ae5ccb9e1d83d", "动效/状态反馈/04-开关过渡.html":"78b24506a79b756967bdddd21f4f41b0ae3b31150e3753b03d4535c4dd39476a", "动效/状态反馈/05-进度确认.html":"91f234875227e34d947ba3481f161cec1ec737fff91b3b6120c7dd35e971fc90"
};
window.ASSET_MANIFEST = {
  version: "0.1.1-seed",
  generatedAt: "2026-07-30",
  integrity: INTEGRITY,
  categories: [
    { id: "sound-press", label: "按压反馈" }, { id: "sound-hover", label: "悬停提示" },
    { id: "sound-toggle", label: "切换状态" }, { id: "motion-enter", label: "进入与层级" },
    { id: "motion-load", label: "加载与等待" }, { id: "motion-state", label: "状态反馈" }
  ],
  items: [
    ...["click1","click2","click3","click4","click5"].map((file, index) => ({ id:`snd-press-0${index+1}`, kind:"audio", category:"sound-press", name:`按压 ${String(index+1).padStart(2,"0")}`, path:`音效/按压/${file}.wav`, license:"CC0-1.0", origin:"Calinou/kenney-ui-audio@8c3d81b", note:["轻量主操作","确认操作对照","次级操作对照","工具型界面对照","快节奏操作对照"][index], tags:["声音","按钮","反馈","clean"] })),
    ...["rollover1","rollover2","rollover3","rollover4","rollover5"].map((file, index) => ({ id:`snd-hover-0${index+1}`, kind:"audio", category:"sound-hover", name:`悬停 ${String(index+1).padStart(2,"0")}`, path:`音效/悬停/${file}.wav`, license:"CC0-1.0", origin:"Calinou/kenney-ui-audio@8c3d81b", note:["可发现性提示","低干扰悬停","密集工具栏","轻松语境","精细控件"][index], tags:["声音","悬停","探索","hover"] })),
    ...["switch1","switch2","switch3","switch4","switch5"].map((file, index) => ({ id:`snd-toggle-0${index+1}`, kind:"audio", category:"sound-toggle", name:`切换 ${String(index+1).padStart(2,"0")}`, path:`音效/切换/${file}.wav`, license:"CC0-1.0", origin:"Calinou/kenney-ui-audio@8c3d81b", note:["开关开启","低强调状态变化","可感知开关","设置界面","模式切换"][index], tags:["声音","开关","状态","toggle"] })),
    { id:"mot-enter-01", kind:"motion", category:"motion-enter", name:"柔和上浮", path:"动效/进入与层级/01-柔和上浮.html", license:"CC0-1.0", origin:"本库原创 CSS motion", note:"首屏内容出现", tags:["motion","entry","calm","onboarding"] },
    { id:"mot-enter-02", kind:"motion", category:"motion-enter", name:"左右揭示", path:"动效/进入与层级/02-左右揭示.html", license:"CC0-1.0", origin:"本库原创 CSS motion", note:"相邻内容切换", tags:["motion","entry","clean","flow"] },
    { id:"mot-enter-03", kind:"motion", category:"motion-enter", name:"焦点缩放", path:"动效/进入与层级/03-焦点缩放.html", license:"CC0-1.0", origin:"本库原创 CSS motion", note:"模态焦点", tags:["motion","entry","crisp","dialog"] },
    { id:"mot-enter-04", kind:"motion", category:"motion-enter", name:"叠层展开", path:"动效/进入与层级/04-叠层展开.html", license:"CC0-1.0", origin:"本库原创 CSS motion", note:"卡片层级解释", tags:["motion","entry","technical","stack"] },
    { id:"mot-enter-05", kind:"motion", category:"motion-enter", name:"阶梯入场", path:"动效/进入与层级/05-阶梯入场.html", license:"CC0-1.0", origin:"本库原创 CSS motion", note:"列表渐进呈现", tags:["motion","entry","ordered","list"] },
    { id:"mot-load-01", kind:"motion", category:"motion-load", name:"轨道循环", path:"动效/加载与等待/01-轨道循环.html", license:"CC0-1.0", origin:"本库原创 CSS motion", note:"持续等待", tags:["motion","loading","technical","waiting"] },
    { id:"mot-load-02", kind:"motion", category:"motion-load", name:"呼吸点", path:"动效/加载与等待/02-呼吸点.html", license:"CC0-1.0", origin:"本库原创 CSS motion", note:"短时等待", tags:["motion","loading","soft","waiting"] },
    { id:"mot-load-03", kind:"motion", category:"motion-load", name:"节奏省略号", path:"动效/加载与等待/03-节奏省略号.html", license:"CC0-1.0", origin:"本库原创 CSS motion", note:"内容生成中", tags:["motion","loading","clean","typing"] },
    { id:"mot-load-04", kind:"motion", category:"motion-load", name:"扫描线", path:"动效/加载与等待/04-扫描线.html", license:"CC0-1.0", origin:"本库原创 CSS motion", note:"数据处理状态", tags:["motion","loading","precise","processing"] },
    { id:"mot-load-05", kind:"motion", category:"motion-load", name:"进度填充", path:"动效/加载与等待/05-进度填充.html", license:"CC0-1.0", origin:"本库原创 CSS motion", note:"可估计的等待", tags:["motion","loading","clear","progress"] },
    { id:"mot-state-01", kind:"motion", category:"motion-state", name:"成功收束", path:"动效/状态反馈/01-成功收束.html", license:"CC0-1.0", origin:"本库原创 CSS motion", note:"已完成确认", tags:["motion","success","assured","confirmation"] },
    { id:"mot-state-02", kind:"motion", category:"motion-state", name:"错误回弹", path:"动效/状态反馈/02-错误回弹.html", license:"CC0-1.0", origin:"本库原创 CSS motion", note:"输入校验失败", tags:["motion","error","direct","validation"] },
    { id:"mot-state-03", kind:"motion", category:"motion-state", name:"提示波纹", path:"动效/状态反馈/03-提示波纹.html", license:"CC0-1.0", origin:"本库原创 CSS motion", note:"新信息提醒", tags:["motion","notice","bright","notification"] },
    { id:"mot-state-04", kind:"motion", category:"motion-state", name:"开关过渡", path:"动效/状态反馈/04-开关过渡.html", license:"CC0-1.0", origin:"本库原创 CSS motion", note:"二元状态切换", tags:["motion","toggle","clean","state"] },
    { id:"mot-state-05", kind:"motion", category:"motion-state", name:"进度确认", path:"动效/状态反馈/05-进度确认.html", license:"CC0-1.0", origin:"本库原创 CSS motion", note:"长任务完成感", tags:["motion","progress","clear","upload"] }
  ]
};
