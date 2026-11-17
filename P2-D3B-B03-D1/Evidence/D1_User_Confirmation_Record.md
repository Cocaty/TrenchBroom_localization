# D1_User_Confirmation_Record — 用户确认状态记录（不得伪造）

## 本轮（B03-D1）用户确认
**无。**

用户在本轮任务书中明确要求：第五节列出的是“本轮的推荐候选，不是用户已经确认的正式译文”，并要求“所有 20 条都必须进入决策表”“不得把 AI 推荐伪装为用户确认”。因此：

- 20/20 条状态：`PROPOSED_PENDING_USER_CONFIRMATION`
- 0 条 `USER_CONFIRMED`
- 0 条 `FINAL_FROZEN`
- 0 条 `NEEDS_REVISION`

## 历史已确认依据（仅用于术语继承，不等于 B03 译文已确认）
| 术语 | 历史来源 | 可继承内容 |
|---|---|---|
| Wavefront OBJ 保留英文 | B01-T2 / B01 术语决策 R1-A1 | 格式名保留，不译作中文格式名 |
| Material Collections → 材质集合 | B01-T2 | material 译作“材质”，但 texture 仍须区分 |
| Open Map → 打开地图 | B02-D1（USER_CONFIRMED） | **仅此一条译文**；不冻结 game path 或 game directory |

## 需用户重点确认的术语组
1. Game path / Game directory：两条统一为“游戏目录”还是“游戏路径”
2. Export path：采用源码修正推荐“相对于导出目录”，还是保留“相对于导出路径”
3. Texture / Material：Texture Paths 定为“纹理路径”，tooltip 同步
4. Crash / Issue：崩溃报告、问题报告、报告问题按钮的措辞
5. AboutDialog：“第三方库、工具与资源”分节标题

**本轮没有任何 B03 译文被正式冻结；下一步 T2 写入必须另行授权。**
