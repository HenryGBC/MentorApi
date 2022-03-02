-- upgrade --
ALTER TABLE "mentor" ADD "value" VARCHAR(120) NOT NULL;
-- downgrade --
ALTER TABLE "mentor" DROP COLUMN "value";
