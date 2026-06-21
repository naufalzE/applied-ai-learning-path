local ReplicatedStorage = game:GetService("ReplicatedStorage")
local Players = game:GetService("Players")

local BattleNPCData = require(ReplicatedStorage:WaitForChild("BattleNPCData"))
local InventoryManager = require(game.ServerScriptService:WaitForChild("InventoryManager"))

local OpenBattleEvent = ReplicatedStorage:WaitForChild("OpenBattleEvent")
local BattleChallengeEvent = ReplicatedStorage:WaitForChild("BattleChallengeEvent")

--------------------------------------------------
-- AUTO-CREATE BATTLENPC
--------------------------------------------------

local map = workspace:WaitForChild("map", 5)

if not map then
	warn("Map folder not found!")
	return
end

-- Hapus yang lama jika ada
local existingNPC = map:FindFirstChild("BattleNPC")
if existingNPC then
	existingNPC:Destroy()
end

-- Buat BattleNPC Model (Warrior style)
local battleNPC = Instance.new("Model")
battleNPC.Name = "BattleNPC"

-- HumanoidRootPart
local hrp = Instance.new("Part")
hrp.Name = "HumanoidRootPart"
hrp.Size = Vector3.new(2, 2, 1)
hrp.Transparency = 1
hrp.Anchored = true
hrp.CanCollide = false
hrp.CFrame = CFrame.new(-20, 1.6, -65)
hrp.Parent = battleNPC

-- Head
local head = Instance.new("Part")
head.Name = "Head"
head.Shape = Enum.PartType.Ball
head.Size = Vector3.new(1.2, 1.2, 1.2)
head.Color = Color3.fromRGB(255, 200, 150)
head.Anchored = true
head.CanCollide = false
head.CFrame = hrp.CFrame * CFrame.new(0, 2.2, 0)
head.Parent = battleNPC

local face = Instance.new("Decal")
face.Face = Enum.NormalId.Front
face.Texture = "rbxassetid://1095999"
face.Parent = head

-- Torso (Gold warrior armor)
local torso = Instance.new("Part")
torso.Name = "Torso"
torso.Size = Vector3.new(2, 2, 1)
torso.Color = Color3.fromRGB(255, 215, 0)
torso.Material = Enum.Material.Neon
 torso.Anchored = true
torso.CanCollide = false
torso.CFrame = hrp.CFrame * CFrame.new(0, 0.5, 0)
torso.Parent = battleNPC

-- Left Arm
local lArm = Instance.new("Part")
lArm.Name = "Left Arm"
lArm.Size = Vector3.new(1, 2, 1)
lArm.Color = Color3.fromRGB(255, 215, 0)
lArm.Material = Enum.Material.Neon
lArm.Anchored = true
lArm.CanCollide = false
lArm.CFrame = hrp.CFrame * CFrame.new(-1.5, 0.5, 0)
lArm.Parent = battleNPC

-- Right Arm
local rArm = Instance.new("Part")
rArm.Name = "Right Arm"
rArm.Size = Vector3.new(1, 2, 1)
rArm.Color = Color3.fromRGB(255, 215, 0)
rArm.Material = Enum.Material.Neon
rArm.Anchored = true
rArm.CanCollide = false
rArm.CFrame = hrp.CFrame * CFrame.new(1.5, 0.5, 0)
rArm.Parent = battleNPC

-- Left Leg
local lLeg = Instance.new("Part")
lLeg.Name = "Left Leg"
lLeg.Size = Vector3.new(1, 2, 1)
lLeg.Color = Color3.fromRGB(40, 40, 40)
lLeg.Anchored = true
lLeg.CanCollide = false
lLeg.CFrame = hrp.CFrame * CFrame.new(-0.5, -1.5, 0)
lLeg.Parent = battleNPC

-- Right Leg
local rLeg = Instance.new("Part")
rLeg.Name = "Right Leg"
rLeg.Size = Vector3.new(1, 2, 1)
rLeg.Color = Color3.fromRGB(40, 40, 40)
rLeg.Anchored = true
rLeg.CanCollide = false
rLeg.CFrame = hrp.CFrame * CFrame.new(0.5, -1.5, 0)
rLeg.Parent = battleNPC

-- Warrior Helmet
local helmet = Instance.new("Part")
helmet.Name = "Helmet"
helmet.Shape = Enum.PartType.Cylinder
helmet.Size = Vector3.new(1.4, 1.4, 0.5)
helmet.Color = Color3.fromRGB(255, 215, 0)
helmet.Material = Enum.Material.Neon
helmet.Anchored = true
helmet.CanCollide = false
helmet.CFrame = head.CFrame * CFrame.new(0, 0.5, 0) * CFrame.Angles(math.rad(90), 0, 0)
helmet.Parent = battleNPC

-- Sword on back
local sword = Instance.new("Part")
sword.Name = "Sword"
sword.Size = Vector3.new(0.2, 0.3, 5)
sword.Color = Color3.fromRGB(200, 200, 200)
sword.Material = Enum.Material.Metal
sword.Anchored = true
sword.CanCollide = false
sword.CFrame = hrp.CFrame * CFrame.new(0, 1.5, 1) * CFrame.Angles(math.rad(-10), 0, 0)
sword.Parent = battleNPC

-- Sword handle
local handle = Instance.new("Part")
handle.Name = "SwordHandle"
handle.Size = Vector3.new(0.3, 0.3, 1)
handle.Color = Color3.fromRGB(139, 69, 19)
handle.Anchored = true
handle.CanCollide = false
handle.CFrame = hrp.CFrame * CFrame.new(0, -0.5, 1.5)
handle.Parent = battleNPC

-- Humanoid
local humanoid = Instance.new("Humanoid")
humanoid.Parent = battleNPC

battleNPC.PrimaryPart = hrp
battleNPC.Parent = map

-- BillboardGui (Nama di atas)
local billboard = Instance.new("BillboardGui")
billboard.Name = "NameTag"
billboard.Size = UDim2.new(0, 200, 0, 50)
billboard.StudsOffset = Vector3.new(0, 5, 0)
billboard.AlwaysOnTop = true
billboard.Parent = head

local nameLabel = Instance.new("TextLabel")
nameLabel.Name = "NameLabel"
nameLabel.Size = UDim2.new(1, 0, 1, 0)
nameLabel.BackgroundTransparency = 1
nameLabel.Text = "The Chosen One"
nameLabel.TextColor3 = Color3.fromRGB(255, 215, 0)
nameLabel.TextStrokeTransparency = 0
nameLabel.TextScaled = true
nameLabel.Font = Enum.Font.GothamBold
nameLabel.Parent = billboard

-- ProximityPrompt (Tekan E)
local prompt = Instance.new("ProximityPrompt")
prompt.Name = "BattlePrompt"
prompt.ActionText = "Battle"
prompt.ObjectText = "The Chosen One"
prompt.HoldDuration = 0
prompt.MaxActivationDistance = 15
prompt.KeyboardKeyCode = Enum.KeyCode.E
prompt.Parent = battleNPC

print("BattleNPC auto-created at:", hrp.Position)

--------------------------------------------------
-- NPC INFO
--------------------------------------------------

local function GetNPCInfo()
	return BattleNPCData.GetNPCInfo()
end

--------------------------------------------------
-- TRIGGER: PROXIMITY PROMPT
--------------------------------------------------

prompt.Triggered:Connect(function(player)

	print(player.Name .. " wants to battle The Chosen One!")

	local npcInfo = GetNPCInfo()
	local playerPet = InventoryManager.GetEquippedPet(player)
	local playerWearer = InventoryManager.GetEquippedWearer(player)

	local playerInfo = {
		Name = player.Name,
		PetName = playerPet and playerPet.Name or "No Pet",
		PetPower = playerPet and playerPet.BasePower or 0,
		WearerBuff = playerWearer and playerWearer.BuffValue or 0,
		TotalWins = playerPet and playerPet.TotalWins or 0
	}

	OpenBattleEvent:FireClient(player, npcInfo, playerInfo)

	print("Data sent to client:", player.Name)

end)

--------------------------------------------------
-- BATTLE CHALLENGE
--------------------------------------------------

BattleChallengeEvent.OnServerEvent:Connect(function(player)

	local npcInfo = GetNPCInfo()
	local playerPet = InventoryManager.GetEquippedPet(player)

	if not playerPet then
		warn("Player has no equipped pet!")
		BattleChallengeEvent:FireClient(player, false, "No Pet Equipped!")
		return
	end

	-- Battle: Best of 5
	local playerScore = 0
	local npcScore = 0
	local rounds = {}

	for round = 1, 5 do

		-- Player roll
		local playerRoll = math.random(1, 100)
		local playerTotal = playerRoll + playerPet.BasePower

		-- Add wearer buff
		local playerWearer = InventoryManager.GetEquippedWearer(player)
		if playerWearer then
			playerTotal += playerWearer.BuffValue
		end

		-- NPC roll
		local npcRoll = math.random(1, 100)
		local npcTotal = npcRoll + npcInfo.Power

		-- Determine winner
		local winner
		if playerTotal > npcTotal then
			winner = "Player"
			playerScore += 1
		elseif npcTotal > playerTotal then
			winner = "NPC"
			npcScore += 1
		else
			winner = "Draw"
		end

		table.insert(rounds, {
			Round = round,
			PlayerRoll = playerRoll,
			PlayerTotal = playerTotal,
			NPCRoll = npcRoll,
			NPCTotal = npcTotal,
			Winner = winner
		})

		-- Check if someone already won 3 rounds
		if playerScore >= 3 or npcScore >= 3 then
			break
		end

	end

	-- Determine battle winner
	local battleWinner
	local battleResult

	if playerScore > npcScore then
		battleWinner = "Player"
		battleResult = "WIN"

		-- Update player pet wins
		playerPet.TotalWins += 1

		-- NPC Level Up (becomes stronger)
		BattleNPCData.LevelUp()

	elseif npcScore > playerScore then
		battleWinner = "NPC"
		battleResult = "LOSE"
	else
		battleWinner = "Draw"
		battleResult = "DRAW"
	end

	-- Ambil NPC info TERBARU setelah level up
	local updatedNPCInfo = GetNPCInfo()

	-- Send result to client dengan UpdatedNPC
	BattleChallengeEvent:FireClient(player, true, {
		Result = battleResult,
		PlayerScore = playerScore,
		NPCScore = npcScore,
		Rounds = rounds,
		NPCLvUp = battleWinner == "Player",
		UpdatedNPC = updatedNPCInfo
	})

	print("BATTLE RESULT:", player.Name, "vs", npcInfo.Name, "-", battleResult)
	if battleWinner == "Player" then
		print("NPC Leveled Up to:", updatedNPCInfo.Level, "Power:", updatedNPCInfo.Power)
	end

end)

--------------------------------------------------
-- AUTO-SAVE (DI LUAR EVENT HANDLER!)
--------------------------------------------------

-- Auto-save saat server shutdown
game:BindToClose(function()
	print("Server shutting down, saving NPC data...")
	BattleNPCData.SaveNPCData()
end)

-- Auto-save setiap 5 menit
task.spawn(function()
	while true do
		task.wait(300) -- 5 menit
		BattleNPCData.SaveNPCData()
	end
end)

print("BattleNPCHandler fully loaded!")

